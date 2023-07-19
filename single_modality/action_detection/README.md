# Action Detection

## Installation

Please follow the installation instructions in [INSTALL](../INSTALL.md).

:warning: Note that you have to set ava datapath `DATA_DIR` in `alphaction/config/paths_catalog.py`.

## Datasets

You can find the dataset instructions in [DATASET](../DATASET.md).

## Model ZOO

| Model    | Setting  | #Frame   | mAP  | Model  | Shell  | Log  |
| -------- | -------  | -------- | ------ | ------ | ------ | ---- |
| UMT-B/16 | K710 PT+FT  | 8    | 33.5 | [ckpt](https://pjlab-gvm-data.oss-cn-shanghai.aliyuncs.com/umt/single_modality/b16_ptk710_ftk710_ftava_f8_res224.pth) | [run.sh](./exp/b16_ptk710_ftk710_ftava_f8_res224.sh) | [log](https://pjlab-gvm-data.oss-cn-shanghai.aliyuncs.com/umt/single_modality/b16_ptk710_ftk710_ftava_f8_res224.txt) |
| UMT-L/16 | K710 PT+FT  | 8    | 39.8 | [ckpt](https://pjlab-gvm-data.oss-cn-shanghai.aliyuncs.com/umt/single_modality/l16_ptk710_ftk710_ftava_f8_res224.pth) | [run.sh](./exp/l16_ptk710_ftk710_ftava_f8_res224.sh) | [log](https://pjlab-gvm-data.oss-cn-shanghai.aliyuncs.com/umt/single_modality/l16_ptk710_ftk710_ftava_f8_res224.txt) |


## Finetuning

For finetuning, you can simply run the pretraining scripts in `exp` as follows:
```shell
bash ./exp/b16_ptk710_ftk710_ftava_f8_res224.sh
```

:warning: **Notes:**
1. Chage `MODEL_PATH` to your model path.
2. For ViT-L, we set `--close_amp` to close amp for stable finetuning.
3. Since we pretrain the models on Kinetics with sparse sampling, the frame span should be similar for better performance. Thus we set `--sparse` to use a large frame span 300, which is equal to the average frame number of Kinetics clips.