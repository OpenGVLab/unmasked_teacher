# Single-modality

## Installation

Please follow the installation instructions in [INSTALL](./INSTALL.md).

## Datasets

You can find the dataset instructions in [DATASET](./DATASET.md).

## Model ZOO

You can find all the models and the scripts in [MODEL_ZOO](./MODEL_ZOO.md).

## Pre-Training

We use [CLIP](https://github.com/openai/CLIP) pretrained models as the unmasked teachers by default:
- Follow [extract.ipynb](./models/extract_clip/extract.ipynb) to extract visual encoder from CLIP.
- Change `MODEL_PATH` in [clip.py](./models/clip.py).

For training, you can simply run the pretraining scripts in `exp/pretraining` as follows:
```shell
bash ./exp/pretraining/b16_ptk710_e200_f8_res224.sh
```

:warning: **Notes:**
1. Chage `DATA_PATH` to your data path before running the scripts.
2. `--sampling_rate` is set to 1 for **sprase sampling**.
3. The latest checkpoint will be automatically saved while training, thus we use a large `--save_ckpt_freq`.
4. For UMT-B/16, we use CLIP-B/16 as the teacher. While for UMT-L/16, we use CLIP-L/14 as the teacher and the **input resolution is set to 196**.


## Finetuning

For finetuning, you can simply run the pretraining scripts in `exp/finetuning` as follows:
```shell
bash ./exp/finetuning/k400/b16_ptk710_ftk710_ftk400_f8_res224.sh
```

:warning: **Notes:**
1. Chage `DATA_PATH` And `PREFIX` to your data path before running the scripts.
2. Chage `MODEL_PATH` to your model path.
3. Set `--use_checkpoint` and `--checkpoint_num` to save GPU memory.
4. The best checkpoint will be automatically evaluated with `--test_best`.
5. Set `--test_num_segment` and `--test_num_crop` for different evaluation strategies.
6. To only run evaluation, just set `--eval`.
