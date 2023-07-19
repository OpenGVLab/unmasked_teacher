# Multi-modality

## Installation

Please follow the installation instructions in [INSTALL](./INSTALL.md).

>The codebase support using [wandb](https://wandb.ai/) to monitor training. If you want to use wandb, you will need to set up it following [this very short instruction](https://docs.wandb.ai/quickstart#1.-set-up-wandb), and also set `wandb.enable` in the config to be `True`. `wandb.entity` and `wandb.project` should also be set.

## Datasets

You can find the dataset instructions in [DATASET](DATASET.md). We have provide all the metadata files of our data.

## Model ZOO

You can find all the models and the scripts in [MODEL_ZOO](./MODEL_ZOO.md).

## Pre-Training

We use [CLIP](https://github.com/openai/CLIP) pretrained models as the unmasked teachers by default:
- Follow [extract.ipynb](../single_modality/models/extract_clip/extract.ipynb) to extract visual encoder from CLIP.
- Change `MODEL_PATH` in [clip.py](./models/backbones/vit/clip.py).

For training, you can simply run the pretraining scripts in `exp/pretraining` as follows:
```shell
bash ./exp/pretraining/b16_ptk710_e200_f8_res224.sh
```

:warning: **Notes:**
1. Set `data_dir` and `your_data_path` like `your_webvid_path` in [data.py](./configs/data.py) before running the scripts.
2. Set `vision_encoder.pretrained` in `vision_encoder.pretrained` in the corresponding config files.
3. Set `--rdzv_endpoint` to your `MASTER_NODE:MASTER_PORT`. You can also use the following commond to automatically set it:
    ```shell
    MASTER_NODE=$(scontrol show hostnames "$SLURM_JOB_NODELIST" | head -n 1)
    ALL_NODES=$(scontrol show hostnames "$SLURM_JOB_NODELIST")
    MASTER_PORT=$((10000 + $RANDOM % 100))
    torchrun --rdzv_endpoint=${MASTER_NODE}:10068 $@
    ```
4. `save_latest=True` will automatically save the latest checkpoint while training.
5. `auto_resume=True` will automatically loaded the best or latest checkpoint while training.


## Zero-shot Evaluation

For zero-shot evaluation, you can simply run the pretraining scripts in `exp/zero_shot` as follows:
```shell
bash ./exp/zero_shot/ret_msrvtt/b16_25m.sh
```

:warning: **Notes:**
1. Set `your_model_path` in the running scripts before running the scripts.
2. Set `zero_shot=True` and `evaluate=True` for zero-shot evaluation 


## Finetuning

For finetuning, you can simply run the pretraining scripts in `exp/finetuning` as follows:
```shell
bash ./exp/finetuning/ret_msrvtt/b16_25m.sh
```

:warning: **Notes:**
1. Set `your_model_path` in the running scripts before running the scripts.