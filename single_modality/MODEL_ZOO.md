# Model Zoo

## Note

- For all the pretraining and finetuning, we adopt spaese/uniform sampling.
- `#Frame` $=$ `#input_frame` $\times$ `#crop` $\times$ `#clip`
- `#input_frame` means how many frames are input for model per inference
- `#crop` means spatial crops (e.g., 3 for left/right/center)
- `#clip` means temporal clips (e.g., 4 means repeted sampling four clips with different start indices)

## Pretraining

| Model    | Setting     | Model  | Shell  | Log  |
| -------- | ----------- | ------ | ------ | ---- |
| UMT-B/16 | K710 200e   |  [ckpt](https://pjlab-gvm-data.oss-cn-shanghai.aliyuncs.com/umt/single_modality/b16_ptk710_f8_res224.pth) | [run.sh](./exp/pretraining/b16_ptk710_f8_res224.sh) | [log](https://pjlab-gvm-data.oss-cn-shanghai.aliyuncs.com/umt/single_modality/b16_ptk710_f8_res224.txt) |
| UMT-L/16 | K710 200e   |  [ckpt](https://pjlab-gvm-data.oss-cn-shanghai.aliyuncs.com/umt/single_modality/l16_ptk710_f8_res224.pth) | [run.sh](./exp/pretraining/l16_ptk710_f8_res224.sh) | [log](https://pjlab-gvm-data.oss-cn-shanghai.aliyuncs.com/umt/single_modality/l16_ptk710_f8_res224.txt) |

## Finetuning

### K710

| Model    | Setting  | #Frame   | Top-1  | Model  | Shell  | Log  |
| -------- | -------  | -------- | ------ | ------ | ------ | ---- |
| UMT-B/16 | K710 PT  | 8x3x4    | 81.9 | [ckpt](https://pjlab-gvm-data.oss-cn-shanghai.aliyuncs.com/umt/single_modality/b16_ptk710_ftk710_f8_res224.pth) | [run.sh](./exp/finetuning/k710/b16_ptk710_ftk710_f8_res224.sh) | [log](https://pjlab-gvm-data.oss-cn-shanghai.aliyuncs.com/umt/single_modality/b16_ptk710_ftk710_f8_res224.txt) |
| UMT-L/16 | K710 PT  | 8x3x4    | 86.0 | [ckpt](https://pjlab-gvm-data.oss-cn-shanghai.aliyuncs.com/umt/single_modality/l16_ptk710_ftk710_f8_res224.pth) | [run.sh](./exp/finetuning/k710/l16_ptk710_ftk710_f8_res224.sh) | [log](https://pjlab-gvm-data.oss-cn-shanghai.aliyuncs.com/umt/single_modality/l16_ptk710_ftk710_f8_res224.txt) |


### K400

| Model    | Setting       | #Frame   | Top-1  | Model  | Shell  | Log  |
| -------- | ------------- | -------- | ------ | ------ | ------ | ---- |
| UMT-B/16 | K710 PT+FT    | 8x3x4    | 87.4 | [ckpt](https://pjlab-gvm-data.oss-cn-shanghai.aliyuncs.com/umt/single_modality/b16_ptk710_ftk710_ftk400_f8_res224.pth) | [run.sh](./exp/finetuning/k400/b16_ptk710_ftk710_ftk400_f8_res224.sh) | [log](https://pjlab-gvm-data.oss-cn-shanghai.aliyuncs.com/umt/single_modality/b16_ptk710_ftk710_ftk400_f8_res224.txt) |
| UMT-L/16 | K710 PT+FT    | 8x3x4    | 90.3 | [ckpt](https://pjlab-gvm-data.oss-cn-shanghai.aliyuncs.com/umt/single_modality/l16_ptk710_ftk710_ftk400_f8_res224.pth) | [run.sh](./exp/finetuning/k400/l16_ptk710_ftk710_ftk400_f8_res224.sh) | [log](https://pjlab-gvm-data.oss-cn-shanghai.aliyuncs.com/umt/single_modality/b16_ptk710_ftk710_ftk400_f8_res224.txt) |
| UMT-L/16 | K710 PT+FT    | 16x3x4   | 90.6 | [ckpt](https://pjlab-gvm-data.oss-cn-shanghai.aliyuncs.com/umt/single_modality/l16_ptk710_ftk710_ftk400_f16_res224.pth) | [run.sh](./exp/finetuning/k400/l16_ptk710_ftk710_ftk400_f16_res224.sh) | [log](https://pjlab-gvm-data.oss-cn-shanghai.aliyuncs.com/umt/single_modality/l16_ptk710_ftk710_ftk400_f16_res224.txt) |


### K600

| Model    | Setting       | #Frame   | Top-1  | Model  | Shell  | Log  |
| -------- | ------------- | -------- | ------ | ------ | ------ | ---- |
| UMT-B/16 | K710 PT+FT    | 8x3x4    | 87.8 | [ckpt](https://pjlab-gvm-data.oss-cn-shanghai.aliyuncs.com/umt/single_modality/b16_ptk710_ftk710_ftk600_f8_res224.pth) | [run.sh](./exp/finetuning/k600/b16_ptk710_ftk710_ftk600_f8_res224.sh) | [log](https://pjlab-gvm-data.oss-cn-shanghai.aliyuncs.com/umt/single_modality/b16_ptk710_ftk710_ftk600_f8_res224.txt) |
| UMT-L/16 | K710 PT+FT    | 8x3x4    | 90.4 | [ckpt](https://pjlab-gvm-data.oss-cn-shanghai.aliyuncs.com/umt/single_modality/l16_ptk710_ftk710_ftk600_f8_res224.pth) | [run.sh](./exp/finetuning/k600/l16_ptk710_ftk710_ftk600_f8_res224.sh) | [log](https://pjlab-gvm-data.oss-cn-shanghai.aliyuncs.com/umt/single_modality/l16_ptk710_ftk710_ftk600_f8_res224.txt) |
| UMT-L/16 | K710 PT+FT    | 16x3x4   | 90.5 | [ckpt](https://pjlab-gvm-data.oss-cn-shanghai.aliyuncs.com/umt/single_modality/l16_ptk710_ftk710_ftk600_f16_res224.pth) | [run.sh](./exp/finetuning/k600/l16_ptk710_ftk710_ftk600_f16_res224.sh) | [log](https://pjlab-gvm-data.oss-cn-shanghai.aliyuncs.com/umt/single_modality/l16_ptk710_ftk710_ftk600_f16_res224.txt) |


### K700

| Model    | Setting       | #Frame   | Top-1  | Model  | Shell  | Log  |
| -------- | ------------- | -------- | ------ | ------ | ------ | ---- |
| UMT-B/16 | K710 PT+FT    | 8x3x4    | 78.5 | [ckpt](https://pjlab-gvm-data.oss-cn-shanghai.aliyuncs.com/umt/single_modality/b16_ptk710_ftk710_ftk700_f8_res224.pth) | [run.sh](./exp/finetuning/k700/b16_ptk710_ftk710_ftk700_f8_res224.sh) | [log](https://pjlab-gvm-data.oss-cn-shanghai.aliyuncs.com/umt/single_modality/b16_ptk710_ftk710_ftk700_f8_res224.txt) |
| UMT-L/16 | K710 PT+FT    | 8x3x4    | 83.2 | [ckpt](https://pjlab-gvm-data.oss-cn-shanghai.aliyuncs.com/umt/single_modality/l16_ptk710_ftk710_ftk700_f8_res224.pth) | [run.sh](./exp/finetuning/k700/l16_ptk710_ftk710_ftk700_f8_res224.sh) | [log](https://pjlab-gvm-data.oss-cn-shanghai.aliyuncs.com/umt/single_modality/l16_ptk710_ftk710_ftk700_f8_res224.txt) |
| UMT-L/16 | K710 PT+FT    | 16x3x4   | 83.6 | [ckpt](https://pjlab-gvm-data.oss-cn-shanghai.aliyuncs.com/umt/single_modality/l16_ptk710_ftk710_ftk700_f16_res224.pth) | [run.sh](./exp/finetuning/k700/l16_ptk710_ftk710_ftk700_f16_res224.sh) | [log](https://pjlab-gvm-data.oss-cn-shanghai.aliyuncs.com/umt/single_modality/l16_ptk710_ftk710_ftk700_f16_res224.txt) |


### MiT V1

| Model         | Setting              | #Frame   | Top-1  | Model  | Shell  | Log  |
| ------------- | -------------------- | -------- | ------ | ------ | ------ | ---- |
| UMT-B/16      | K710 PT+FT, K400 FT  | 8x3x4    | 44.6 | [ckpt](https://pjlab-gvm-data.oss-cn-shanghai.aliyuncs.com/umt/single_modality/b16_ptk710_ftk710_ftk400_ftmitv1_f8_res224.pth) | [run.sh](./exp/finetuning/mitv1/b16_ptk710_ftk710_ftk400_ftmitv1_f8_res224.sh) | [log](https://pjlab-gvm-data.oss-cn-shanghai.aliyuncs.com/umt/single_modality/b16_ptk710_ftk710_ftk400_ftmitv1_f8_res224.txt) |
| UMT-L/16 384↑ | K710 PT+FT, K400 FT  | 8x3x4    | 45.5 | [ckpt](https://pjlab-gvm-data.oss-cn-shanghai.aliyuncs.com/umt/single_modality/b16_ptk710_ftk710_ftk400_ftmitv1_f8_res384.pth) | [run.sh](./exp/finetuning/mitv1/b16_ptk710_ftk710_ftk400_ftmitv1_f8_res384.sh) | [log](https://pjlab-gvm-data.oss-cn-shanghai.aliyuncs.com/umt/single_modality/b16_ptk710_ftk710_ftk400_ftmitv1_f8_res384.txt) |
| UMT-L/16      | K710 PT+FT, K400 FT  | 16x3x4   | 48.0 | [ckpt](https://pjlab-gvm-data.oss-cn-shanghai.aliyuncs.com/umt/single_modality/l16_ptk710_ftk710_ftk400_ftmitv1_f8_res224.pth) | [run.sh](./exp/finetuning/mitv1/l16_ptk710_ftk710_ftk400_ftmitv1_f8_res224.sh) | [log](https://pjlab-gvm-data.oss-cn-shanghai.aliyuncs.com/umt/single_modality/l16_ptk710_ftk710_ftk400_ftmitv1_f8_res224.txt) |
| UMT-L/16 384↑ | K710 PT+FT, K400 FT  | 16x3x4   | 48.7 | [ckpt](https://pjlab-gvm-data.oss-cn-shanghai.aliyuncs.com/umt/single_modality/l16_ptk710_ftk710_ftk400_ftmitv1_f8_res384.pth) | [run.sh](./exp/finetuning/mitv1/l16_ptk710_ftk710_ftk400_ftmitv1_f8_res384.sh) | [log](https://pjlab-gvm-data.oss-cn-shanghai.aliyuncs.com/umt/single_modality/l16_ptk710_ftk710_ftk400_ftmitv1_f8_res384.pth) |


### SthSth V2

| Model    | Setting     | #Frame   | Top-1  | Model  | Shell  | Log  |
| -------- | ----------- | -------- | ------ | ------ | ------ | ---- |
| UMT-B/16 | K710 PT     | 8x3x4    | 70.8 | [ckpt](https://pjlab-gvm-data.oss-cn-shanghai.aliyuncs.com/umt/single_modality/b16_ptk710_ftk710_ftssv2_f8_res224.pth) | [run.sh](./exp/finetuning/ssv2/b16_ptk710_ftk710_ftssv2_f8_res224.sh) | [log](https://pjlab-gvm-data.oss-cn-shanghai.aliyuncs.com/umt/single_modality/b16_ptk710_ftk710_ftssv2_f8_res224.txt) |
| UMT-L/16 | K710 PT     | 8x3x4    | 74.7 | [ckpt](https://pjlab-gvm-data.oss-cn-shanghai.aliyuncs.com/umt/single_modality/l16_ptk710_ftk710_ftssv2_f8_res224.pth) | [run.sh](./exp/finetuning/ssv2/l16_ptk710_ftk710_ftssv2_f16_res224.sh) | [log](https://pjlab-gvm-data.oss-cn-shanghai.aliyuncs.com/umt/single_modality/l16_ptk710_ftk710_ftssv2_f8_res224.txt) |


### AVA v2.2

See [action_detection](./action_detection).