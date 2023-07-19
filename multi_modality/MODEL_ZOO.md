# Model Zoo

All the model weights are saved with the `clip_teacher`, which are loaded from the CLIP vision encoder.

## Pretraining

We load those models with K710 pretraining (Stage1) and further pretrain them on multimodality data (Stage2).

- 5M: CC3M + WebVid2M
- 17M: CC3M + CC12M + COCO + VG + SBU + WebVid2M
- 25M: CC3M + CC12M + COCO + VG + SBU + WebVid10M

| Model    | Setting     | Model  | Script  |
| -------- | ----------- | ------ | ------- |
| UMT-B/16 | 5M          |  [ckpt](https://pjlab-gvm-data.oss-cn-shanghai.aliyuncs.com/umt/multi_modality/b16_5m.pth) | [script](./exp/pretraining/b16_5m.sh)  |
| UMT-B/16 | 17M         |  [ckpt](https://pjlab-gvm-data.oss-cn-shanghai.aliyuncs.com/umt/multi_modality/b16_17m.pth) | [script](./exp/pretraining/b16_17m.sh) |
| UMT-B/16 | 25M         |  [ckpt](https://pjlab-gvm-data.oss-cn-shanghai.aliyuncs.com/umt/multi_modality/b16_25m.pth) | [script](./exp/pretraining/b16_25m.sh) |
| UMT-L/16 | 5M          |  [ckpt](https://pjlab-gvm-data.oss-cn-shanghai.aliyuncs.com/umt/multi_modality/l16_5m.pth) | [script](./exp/pretraining/l16_5m.sh)  |
| UMT-L/16 | 17M         |  [ckpt](https://pjlab-gvm-data.oss-cn-shanghai.aliyuncs.com/umt/multi_modality/l16_17m.pth) | [script](./exp/pretraining/l16_17m.sh) |
| UMT-L/16 | 25M         |  [ckpt](https://pjlab-gvm-data.oss-cn-shanghai.aliyuncs.com/umt/multi_modality/l16_25m.pth) | [script](./exp/pretraining/l16_25m.sh) |


### Zero-shot Evaluation

<div align="left">
<table width="100%">
    <tr align="center">
        <th rowspan="2">Dataset</th><th rowspan="2">Retrieval</th><th colspan="3">UMT-B/16</th><th colspan="3">UMT-L/16</th>
    </tr>
    <tr align="center">
        <th>5M</th><th>17M</th><th>25M</th><th>5M</th><th>17M</th><th>25M</th>
    </tr>
    <tr align="center">
        <th rowspan="3">MSRVTT</th>
        <td>T2V</td>
        <td align='left'>R@1: 29.6<br>R@5: 52.8<br>R@10: 61.9<br></td>
        <td align='left'>R@1: 35.5<br>R@5: 59.3<br>R@10: 68.6<br></td>
        <td align='left'>R@1: 35.2<br>R@5: 57.8<br>R@10: 66.0<br></td>
        <td align='left'>R@1: 33.3<br>R@5: 58.1<br>R@10: 66.7<br></td>
        <td align='left'>R@1: 42.6<br>R@5: 64.4<br>R@10: 73.1<br></td>
        <td align='left'>R@1: 40.7<br>R@5: 63.4<br>R@10: 71.8<br></td>
    </tr>
    <tr align="center">
        <td>V2T</td>
        <td align='left'>R@1: 26.2<br>R@5: 46.7<br>R@10: 54.9<br></td>
        <td align='left'>R@1: 31.6<br>R@5: 53.5<br>R@10: 64.1<br></td>
        <td align='left'>R@1: 30.3<br>R@5: 50.7<br>R@10: 61.4<br></td>
        <td align='left'>R@1: 30.2<br>R@5: 51.3<br>R@10: 61.6<br></td>
        <td align='left'>R@1: 38.6<br>R@5: 59.8<br>R@10: 69.6<br></td>
        <td align='left'>R@1: 37.1<br>R@5: 58.7<br>R@10: 68.9<br></td>
    </tr>
    <tr align="center">
        <td>Material</td>
        <td><a href="./exp/zero_shot/ret_msrvtt/b16_5m.sh">script</a></td>
        <td><a href="./exp/zero_shot/ret_msrvtt/b16_17m.sh">script</a></td>
        <td><a href="./exp/zero_shot/ret_msrvtt/b16_25m.sh">script</a></td>
        <td><a href="./exp/zero_shot/ret_msrvtt/l16_5m.sh">script</a></td>
        <td><a href="./exp/zero_shot/ret_msrvtt/l16_17m.sh">script</a></td>
        <td><a href="./exp/zero_shot/ret_msrvtt/l16_25m.sh">script</a></td>
    </tr>
    <tr align="center">
        <th rowspan="3">DiDeMo</th>
        <td>T2V</td>
        <td align='left'>R@1: 33.4<br>R@5: 58.3<br>R@10: 67.0<br></td>
        <td align='left'>R@1: 41.9<br>R@5: 66.7<br>R@10: 75.0<br></td>
        <td align='left'>R@1: 41.2<br>R@5: 65.4<br>R@10: 74.9<br></td>
        <td align='left'>R@1: 34.0<br>R@5: 60.4<br>R@10: 68.7<br></td>
        <td align='left'>R@1: 46.4<br>R@5: 70.0<br>R@10: 78.8<br></td>
        <td align='left'>R@1: 48.6<br>R@5: 72.9<br>R@10: 79.0<br></td>
    </tr>
    <tr align="center">
        <td>V2T</td>
        <td align='left'>R@1: 32.0<br>R@5: 58.7<br>R@10: 68.2<br></td>
        <td align='left'>R@1: 40.3<br>R@5: 66.6<br>R@10: 75.8<br></td>
        <td align='left'>R@1: 40.8<br>R@5: 67.7<br>R@10: 76.7<br></td>
        <td align='left'>R@1: 36.2<br>R@5: 60.0<br>R@10: 68.6<br></td>
        <td align='left'>R@1: 46.5<br>R@5: 72.2<br>R@10: 79.5<br></td>
        <td align='left'>R@1: 49.9<br>R@5: 74.8<br>R@10: 81.4<br></td>
    </tr>
    <tr align="center">
        <td>Material</td>
        <td><a href="./exp/zero_shot/ret_didemo/b16_5m.sh">script</a></td>
        <td><a href="./exp/zero_shot/ret_didemo/b16_17m.sh">script</a></td>
        <td><a href="./exp/zero_shot/ret_didemo/b16_25m.sh">script</a></td>
        <td><a href="./exp/zero_shot/ret_didemo/l16_5m.sh">script</a></td>
        <td><a href="./exp/zero_shot/ret_didemo/l16_17m.sh">script</a></td>
        <td><a href="./exp/zero_shot/ret_didemo/l16_25m.sh">script</a></td>
    </tr>
    <tr align="center">
        <th rowspan="3">ActivityNet</th>
        <td>T2V</td>
        <td align='left'>R@1: 28.3<br>R@5: 53.0<br>R@10: 64.2<br></td>
        <td align='left'>R@1: 33.8<br>R@5: 59.1<br>R@10: 70.4<br></td>
        <td align='left'>R@1: 35.5<br>R@5: 60.6<br>R@10: 71.8<br></td>
        <td align='left'>R@1: 31.9<br>R@5: 60.2<br>R@10: 72.0<br></td>
        <td align='left'>R@1: 42.8<br>R@5: 69.6<br>R@10: 79.8<br></td>
        <td align='left'>R@1: 41.9<br>R@5: 68.9<br>R@10: 80.3<br></td>
    </tr>
    <tr align="center">
        <td>V2T</td>
        <td align='left'>R@1: 25.9<br>R@5: 50.2<br>R@10: 61.7<br></td>
        <td align='left'>R@1: 31.6<br>R@5: 56.2<br>R@10: 67.9<br></td>
        <td align='left'>R@1: 32.8<br>R@5: 57.6<br>R@10: 69.2<br></td>
        <td align='left'>R@1: 30.0<br>R@5: 59.1<br>R@10: 71.3<br></td>
        <td align='left'>R@1: 40.7<br>R@5: 67.6<br>R@10: 78.6<br></td>
        <td align='left'>R@1: 39.4<br>R@5: 66.8<br>R@10: 78.3<br></td>
    </tr>
    <tr align="center">
        <td>Material</td>
        <td><a href="./exp/zero_shot/ret_anet/b16_5m.sh">script</a></td>
        <td><a href="./exp/zero_shot/ret_anet/b16_17m.sh">script</a></td>
        <td><a href="./exp/zero_shot/ret_anet/b16_25m.sh">script</a></td>
        <td><a href="./exp/zero_shot/ret_anet/l16_5m.sh">script</a></td>
        <td><a href="./exp/zero_shot/ret_anet/l16_17m.sh">script</a></td>
        <td><a href="./exp/zero_shot/ret_anet/l16_25m.sh">script</a></td>
    </tr>
    <tr align="center">
        <th rowspan="3">LSMDC</th>
        <td>T2V</td>
        <td align='left'>R@1: 16.8<br>R@5: 30.5<br>R@10: 37.6<br></td>
        <td align='left'>R@1: 18.1<br>R@5: 33.1<br>R@10: 40.0<br></td>
        <td align='left'>R@1: 19.1<br>R@5: 33.4<br>R@10: 42.2<br></td>
        <td align='left'>R@1: 20.0<br>R@5: 37.2<br>R@10: 43.7<br></td>
        <td align='left'>R@1: 25.2<br>R@5: 43.0<br>R@10: 50.5<br></td>
        <td align='left'>R@1: 24.9<br>R@5: 41.7<br>R@10: 51.8<br></td>
    </tr>
    <tr align="center">
        <td>V2T</td>
        <td align='left'>R@1: 12.9<br>R@5: 27.4<br>R@10: 33.6<br></td>
        <td align='left'>R@1: 16.0<br>R@5: 29.9<br>R@10: 35.7<br></td>
        <td align='left'>R@1: 15.7<br>R@5: 30.6<br>R@10: 37.4<br></td>
        <td align='left'>R@1: 16.1<br>R@5: 32.0<br>R@10: 39.2<br></td>
        <td align='left'>R@1: 23.2<br>R@5: 37.7<br>R@10: 44.2<br></td>
        <td align='left'>R@1: 21.9<br>R@5: 37.8<br>R@10: 45.7<br></td>
    </tr>
    <tr align="center">
        <td>Material</td>
        <td><a href="./exp/zero_shot/ret_lsmdc/b16_5m.sh">script</a></td>
        <td><a href="./exp/zero_shot/ret_lsmdc/b16_17m.sh">script</a></td>
        <td><a href="./exp/zero_shot/ret_lsmdc/b16_25m.sh">script</a></td>
        <td><a href="./exp/zero_shot/ret_lsmdc/l16_5m.sh">script</a></td>
        <td><a href="./exp/zero_shot/ret_lsmdc/l16_17m.sh">script</a></td>
        <td><a href="./exp/zero_shot/ret_lsmdc/l16_25m.sh">script</a></td>
    </tr>
    <tr align="center">
        <th rowspan="3">MSVD</th>
        <td>T2V</td>
        <td align='left'>R@1: 55.7<br>R@5: 83.7<br>R@10: 92.2<br></td>
        <td align='left'>R@1: 58.8<br>R@5: 86.1<br>R@10: 91.5<br></td>
        <td align='left'>R@1: 60.3<br>R@5: 86.7<br>R@10: 91.9<br></td>
        <td align='left'>R@1: 68.1<br>R@5: 92.1<br>R@10: 95.2<br></td>
        <td align='left'>R@1: 71.0<br>R@5: 93.3<br>R@10: 96.4<br></td>
        <td align='left'>R@1: 72.2<br>R@5: 94.2<br>R@10: 96.9<br></td>
    </tr>
    <tr align="center">
        <td>V2T</td>
        <td align='left'>R@1: 60.6<br>R@5: 85.7<br>R@10: 92.2<br></td>
        <td align='left'>R@1: 61.9<br>R@5: 86.9<br>R@10: 91.3<br></td>
        <td align='left'>R@1: 64.0<br>R@5: 86.3<br>R@10: 90.4<br></td>
        <td align='left'>R@1: 68.1<br>R@5: 92.5<br>R@10: 96.3<br></td>
        <td align='left'>R@1: 69.1<br>R@5: 91.5<br>R@10: 94.8<br></td>
        <td align='left'>R@1: 72.4<br>R@5: 93.4<br>R@10: 95.8<br></td>
    </tr>
    <tr align="center">
        <td>Material</td>
        <td><a href="./exp/zero_shot/ret_msvd/b16_5m.sh">script</a></td>
        <td><a href="./exp/zero_shot/ret_msvd/b16_17m.sh">script</a></td>
        <td><a href="./exp/zero_shot/ret_msvd/b16_25m.sh">script</a></td>
        <td><a href="./exp/zero_shot/ret_msvd/l16_5m.sh">script</a></td>
        <td><a href="./exp/zero_shot/ret_msvd/l16_17m.sh">script</a></td>
        <td><a href="./exp/zero_shot/ret_msvd/l16_25m.sh">script</a></td>
    </tr>
</table>
<br>
</div>

## Finetuning

### Video-Text Retrieval 

<div align="left">
<table width="100%">
    <tr align="center">
        <th rowspan="2">Dataset</th><th rowspan="2">Retrieval</th><th colspan="3">UMT-B/16</th><th colspan="3">UMT-L/16</th>
    </tr>
    <tr align="center">
        <th>5M</th><th>17M</th><th>25M</th><th>5M</th><th>17M</th><th>25M</th>
    </tr>
    <tr align="center">
        <th rowspan="3">MSRVTT</th>
        <td>T2V</td>
        <td align='left'>R@1: 46.3<br>R@5: 72.7<br>R@10: 82.0<br></td>
        <td align='left'>R@1: 50.6<br>R@5: 75.4<br>R@10: 83.5<br></td>
        <td align='left'>R@1: 51.0<br>R@5: 76.5<br>R@10: 84.2<br></td>
        <td align='left'>R@1: 53.3<br>R@5: 76.6<br>R@10: 83.9<br></td>
        <td align='left'>R@1: 56.5<br>R@5: 80.1<br>R@10: 87.4<br></td>
        <td align='left'>R@1: 58.8<br>R@5: 81.0<br>R@10: 87.1<br></td>
    </tr>
    <tr align="center">
        <td>V2T</td>
        <td align='left'>R@1: 44.4<br>R@5: 72.8<br>R@10: 80.7<br></td>
        <td align='left'>R@1: 49.4<br>R@5: 76.7<br>R@10: 83.5<br></td>
        <td align='left'>R@1: 49.0<br>R@5: 77.0<br>R@10: 84.7<br></td>
        <td align='left'>R@1: 51.4<br>R@5: 76.3<br>R@10: 82.8<br></td>
        <td align='left'>R@1: 56.7<br>R@5: 79.6<br>R@10: 86.7<br></td>
        <td align='left'>R@1: 58.6<br>R@5: 81.6<br>R@10: 86.5<br></td>
    </tr>
    <tr align="center">
        <td>Material</td>
        <td><a href="./exp/finetuning/ret_msrvtt/b16_5m.sh">script</a></td>
        <td><a href="./exp/finetuning/ret_msrvtt/b16_17m.sh">script</a></td>
        <td><a href="./exp/finetuning/ret_msrvtt/b16_25m.sh">script</a><a href="https://pjlab-gvm-data.oss-cn-shanghai.aliyuncs.com/umt/multi_modality/ret_msrvtt_b16_25m.pth"> <b>[ckpt]</b></a></td>
        <td><a href="./exp/finetuning/ret_msrvtt/l16_5m.sh">script</a></td>
        <td><a href="./exp/finetuning/ret_msrvtt/l16_17m.sh">script</a></td>
        <td><a href="./exp/finetuning/ret_msrvtt/l16_25m.sh">script</a><a href="https://pjlab-gvm-data.oss-cn-shanghai.aliyuncs.com/umt/multi_modality/ret_msrvtt_l16_25m.pth"> <b>[ckpt]</b></a></td>
    </tr>
    <tr align="center">
        <th rowspan="3">DiDeMo</th>
        <td>T2V</td>
        <td align='left'>R@1: 54.8<br>R@5: 83.0<br>R@10: 89.0<br></td>
        <td align='left'>R@1: 60.8<br>R@5: 85.1<br>R@10: 91.0<br></td>
        <td align='left'>R@1: 61.6<br>R@5: 86.8<br>R@10: 91.5<br></td>
        <td align='left'>R@1: 59.7<br>R@5: 84.9<br>R@10: 90.8<br></td>
        <td align='left'>R@1: 66.6<br>R@5: 89.9<br>R@10: 93.7<br></td>
        <td align='left'>R@1: 70.4<br>R@5: 90.1<br>R@10: 93.5<br></td>
    </tr>
    <tr align="center">
        <td>V2T</td>
        <td align='left'>R@1: 52.9<br>R@5: 80.2<br>R@10: 85.8<br></td>
        <td align='left'>R@1: 59.5<br>R@5: 83.8<br>R@10: 90.7<br></td>
        <td align='left'>R@1: 59.5<br>R@5: 84.9<br>R@10: 90.5<br></td>
        <td align='left'>R@1: 59.5<br>R@5: 84.5<br>R@10: 90.7<br></td>
        <td align='left'>R@1: 66.4<br>R@5: 87.5<br>R@10: 92.9<br></td>
        <td align='left'>R@1: 65.7<br>R@5: 89.6<br>R@10: 93.3<br></td>
    </tr>
    <tr align="center">
        <td>Material</td>
        <td><a href="./exp/finetuning/ret_didemo/b16_5m.sh">script</a></td>
        <td><a href="./exp/finetuning/ret_didemo/b16_17m.sh">script</a></td>
        <td><a href="./exp/finetuning/ret_didemo/b16_25m.sh">script</a><a href="https://pjlab-gvm-data.oss-cn-shanghai.aliyuncs.com/umt/multi_modality/ret_didemo_b16_25m.pth"> <b>[ckpt]</b></a></td>
        <td><a href="./exp/finetuning/ret_didemo/l16_5m.sh">script</a></td>
        <td><a href="./exp/finetuning/ret_didemo/l16_17m.sh">script</a></td>
        <td><a href="./exp/finetuning/ret_didemo/l16_25m.sh">script</a><a href="https://pjlab-gvm-data.oss-cn-shanghai.aliyuncs.com/umt/multi_modality/ret_didemo_l16_25m.pth"> <b>[ckpt]</b></a></td>
    </tr>
    <tr align="center">
        <th rowspan="3">ActivityNet</th>
        <td>T2V</td>
        <td align='left'>R@1: 52.1<br>R@5: 80.5<br>R@10: 89.6<br></td>
        <td align='left'>R@1: 56.1<br>R@5: 82.5<br>R@10: 91.2<br></td>
        <td align='left'>R@1: 58.3<br>R@5: 83.9<br>R@10: 91.5<br></td>
        <td align='left'>R@1: 58.1<br>R@5: 85.5<br>R@10: 92.9<br></td>
        <td align='left'>R@1: 66.6<br>R@5: 88.6<br>R@10: 94.7<br></td>
        <td align='left'>R@1: 66.8<br>R@5: 89.1<br>R@10: 94.9<br></td>
    </tr>
    <tr align="center">
        <td>V2T</td>
        <td align='left'>R@1: 50.0<br>R@5: 79.8<br>R@10: 88.2<br></td>
        <td align='left'>R@1: 54.6<br>R@5: 82.1<br>R@10: 91.1<br></td>
        <td align='left'>R@1: 56.0<br>R@5: 83.5<br>R@10: 91.7<br></td>
        <td align='left'>R@1: 55.4<br>R@5: 84.4<br>R@10: 92.9<br></td>
        <td align='left'>R@1: 64.3<br>R@5: 87.8<br>R@10: 94.8<br></td>
        <td align='left'>R@1: 64.4<br>R@5: 89.1<br>R@10: 94.8<br></td>
    </tr>
    <tr align="center">
        <td>Material</td>
        <td><a href="./exp/finetuning/ret_anet/b16_5m.sh">script</a></td>
        <td><a href="./exp/finetuning/ret_anet/b16_17m.sh">script</a></td>
        <td><a href="./exp/finetuning/ret_anet/b16_25m.sh">script</a><a href="https://pjlab-gvm-data.oss-cn-shanghai.aliyuncs.com/umt/multi_modality/ret_anet_b16_25m.pth"> <b>[ckpt]</b></a></td>
        <td><a href="./exp/finetuning/ret_anet/l16_5m.sh">script</a></td>
        <td><a href="./exp/finetuning/ret_anet/l16_17m.sh">script</a></td>
        <td><a href="./exp/finetuning/ret_anet/l16_25m.sh">script</a><a href="https://pjlab-gvm-data.oss-cn-shanghai.aliyuncs.com/umt/multi_modality/ret_anet_l16_25m.pth"> <b>[ckpt]</b></a></td>
    </tr>
    <tr align="center">
        <th rowspan="3">LSMDC</th>
        <td>T2V</td>
        <td align='left'>R@1: 30.3<br>R@5: 51.8<br>R@10: 61.4<br></td>
        <td align='left'>R@1: 32.3<br>R@5: 54.5<br>R@10: 61.9<br></td>
        <td align='left'>R@1: 32.7<br>R@5: 54.7<br>R@10: 63.4<br></td>
        <td align='left'>R@1: 37.7<br>R@5: 60.6<br>R@10: 67.3<br></td>
        <td align='left'>R@1: 41.4<br>R@5: 63.8<br>R@10: 72.3<br></td>
        <td align='left'>R@1: 43.0<br>R@5: 65.5<br>R@10: 73.0<br></td>
    </tr>
    <tr align="center">
        <td>V2T</td>
        <td align='left'>R@1: 29.8<br>R@5: 52.2<br>R@10: 60.5<br></td>
        <td align='left'>R@1: 31.5<br>R@5: 53.6<br>R@10: 61.9<br></td>
        <td align='left'>R@1: 32.7<br>R@5: 53.5<br>R@10: 63.2<br></td>
        <td align='left'>R@1: 36.2<br>R@5: 58.9<br>R@10: 65.7<br></td>
        <td align='left'>R@1: 40.3<br>R@5: 63.1<br>R@10: 71.1<br></td>
        <td align='left'>R@1: 41.4<br>R@5: 64.3<br>R@10: 71.5<br></td>
    </tr>
    <tr align="center">
        <td>Material</td>
        <td><a href="./exp/finetuning/ret_lsmdc/b16_5m.sh">script</a></td>
        <td><a href="./exp/finetuning/ret_lsmdc/b16_17m.sh">script</a></td>
        <td><a href="./exp/finetuning/ret_lsmdc/b16_25m.sh">script</a><a href="https://pjlab-gvm-data.oss-cn-shanghai.aliyuncs.com/umt/multi_modality/ret_lsmdc_b16_25m.pth"> <b>[ckpt]</b></a></td>
        <td><a href="./exp/finetuning/ret_lsmdc/l16_5m.sh">script</a></td>
        <td><a href="./exp/finetuning/ret_lsmdc/l16_17m.sh">script</a></td>
        <td><a href="./exp/finetuning/ret_lsmdc/l16_25m.sh">script</a><a href="https://pjlab-gvm-data.oss-cn-shanghai.aliyuncs.com/umt/multi_modality/ret_lsmdc_l16_25m.pth"> <b>[ckpt]</b></a></td>
    </tr>
    <tr align="center">
        <th rowspan="3">MSVD</th>
        <td>T2V</td>
        <td align='left'>R@1: 67.0<br>R@5: 92.7<br>R@10: 96.7<br></td>
        <td align='left'>R@1: 70.8<br>R@5: 93.7<br>R@10: 96.6<br></td>
        <td align='left'>R@1: 71.9<br>R@5: 94.5<br>R@10: 97.8<br></td>
        <td align='left'>R@1: 76.9<br>R@5: 96.7<br>R@10: 98.7<br></td>
        <td align='left'>R@1: 78.8<br>R@5: 97.3<br>R@10: 98.8<br></td>
        <td align='left'>R@1: 80.3<br>R@5: 98.1<br>R@10: 99.0<br></td>
    </tr>
    <tr align="center">
        <td>V2T</td>
        <td align='left'>R@1: 67.0<br>R@5: 92.5<br>R@10: 96.3<br></td>
        <td align='left'>R@1: 71.3<br>R@5: 93.9<br>R@10: 97.2<br></td>
        <td align='left'>R@1: 74.0<br>R@5: 94.6<br>R@10: 97.3<br></td>
        <td align='left'>R@1: 73.6<br>R@5: 96.3<br>R@10: 98.1<br></td>
        <td align='left'>R@1: 78.1<br>R@5: 97.6<br>R@10: 98.7<br></td>
        <td align='left'>R@1: 81.2<br>R@5: 96.7<br>R@10: 98.7<br></td>
    </tr>
    <tr align="center">
        <td>Material</td>
        <td><a href="./exp/finetuning/ret_msvd/b16_5m.sh">script</a></td>
        <td><a href="./exp/finetuning/ret_msvd/b16_17m.sh">script</a></td>
        <td><a href="./exp/finetuning/ret_msvd/b16_25m.sh">script</a><a href="https://pjlab-gvm-data.oss-cn-shanghai.aliyuncs.com/umt/multi_modality/ret_msvd_b16_25m.pth"> <b>[ckpt]</b></a></td>
        <td><a href="./exp/finetuning/ret_msvd/l16_5m.sh">script</a></td>
        <td><a href="./exp/finetuning/ret_msvd/l16_17m.sh">script</a></td>
        <td><a href="./exp/finetuning/ret_msvd/l16_25m.sh">script</a><a href="https://pjlab-gvm-data.oss-cn-shanghai.aliyuncs.com/umt/multi_modality/ret_msvd_l16_25m.pth"> <b>[ckpt]</b></a></td>
    </tr>
    <tr align="center">
        <th rowspan="2">SSV2-<br>label</th>
        <td>T2V</td>
        <td align='left'>R@1: 63.1<br>R@5: 87.1<br>R@10: 92.3<br></td>
        <td align='left'>R@1: 63.4<br>R@5: 88.0<br>R@10: 92.9<br></td>
        <td align='left'>R@1: 64.2<br>R@5: 88.2<br>R@10: 92.7<br></td>
        <td align='left'>R@1: 70.5<br>R@5: 92.3<br>R@10: 9.2<br></td>
        <td align='left'>R@1: 73.1<br>R@5: 93.2<br>R@10: 96.4<br></td>
        <td align='left'>R@1: 73.3<br>R@5: 92.7<br>R@10: 96.9<br></td>
    </tr>
    <tr align="center">
        <td>Material</td>
        <td><a href="./exp/finetuning/ret_ssv2_label/b16_5m.sh">script</a></td>
        <td><a href="./exp/finetuning/ret_ssv2_label/b16_17m.sh">script</a></td>
        <td><a href="./exp/finetuning/ret_ssv2_label/b16_25m.sh">script</a><a href="https://pjlab-gvm-data.oss-cn-shanghai.aliyuncs.com/umt/multi_modality/ret_ssv2_label_b16_25m.pth"> <b>[ckpt]</b></a></td>
        <td><a href="./exp/finetuning/ret_ssv2_label/l16_5m.sh">script</a></td>
        <td><a href="./exp/finetuning/ret_ssv2_label/l16_17m.sh">script</a></td>
        <td><a href="./exp/finetuning/ret_ssv2_label/l16_25m.sh">script</a><a href="https://pjlab-gvm-data.oss-cn-shanghai.aliyuncs.com/umt/multi_modality/ret_ssv2_label_l16_25m.pth"> <b>[ckpt]</b></a></td>
    </tr>
    <tr align="center">
        <th rowspan="2">SSV2-<br>template</th>
        <td>T2V</td>
        <td align='left'>R@1: 87.3<br>R@5: 100<br>R@10: 100<br></td>
        <td align='left'>R@1: 86.8<br>R@5: 99.4<br>R@10: 100<br></td>
        <td align='left'>R@1: 87.9<br>R@5: 99。4<br>R@10: 100<br></td>
        <td align='left'>R@1: 90.2<br>R@5: 99.4<br>R@10: 100<br></td>
        <td align='left'>R@1: 90.8<br>R@5: 100<br>R@10: 100<br></td>
        <td align='left'>R@1: 90.8<br>R@5: 99.4<br>R@10: 100<br></td>
    </tr>
    <tr align="center">
        <td>Material</td>
        <td><a href="./exp/finetuning/ret_ssv2_tpl/b16_5m.sh">script</a></td>
        <td><a href="./exp/finetuning/ret_ssv2_tpl/b16_17m.sh">script</a></td>
        <td><a href="./exp/finetuning/ret_ssv2_tpl/b16_25m.sh">script</a><a href="https://pjlab-gvm-data.oss-cn-shanghai.aliyuncs.com/umt/multi_modality/ret_ssv2_tpl_b16_25m.pth"> <b>[ckpt]</b></a></td>
        <td><a href="./exp/finetuning/ret_ssv2_tpl/l16_5m.sh">script</a></td>
        <td><a href="./exp/finetuning/ret_ssv2_tpl/l16_17m.sh">script</a></td>
        <td><a href="./exp/finetuning/ret_ssv2_tpl/l16_25m.sh">script</a><a href="https://pjlab-gvm-data.oss-cn-shanghai.aliyuncs.com/umt/multi_modality/ret_ssv2_tpl_b16_25m.pth"> <b>[ckpt]</b></a></td>
    </tr>
</table>
<br>
</div>


### Video Question Answering

<div align="left">
<table width="100%">
    <tr align="center">
        <th rowspan="2">Dataset</th><th colspan="3">UMT-B/16</th><th colspan="3">UMT-L/16</th>
    </tr>
    <tr align="center">
        <th>5M</th><th>17M</th><th>25M</th><th>5M</th><th>17M</th><th>25M</th>
    </tr>
    <tr align="center">
        <th rowspan="2">ActivityNet-QA</th>
        <td>43.5</td>
        <td>44.9</td>
        <td>44.8</td>
        <td>45.1</td>
        <td>47.3</td>
        <td>47.9</td>
    </tr>
    <tr align="center">
        <td><a href="./exp/finetuning/qa_anet/b16_5m.sh">script</a></td>
        <td><a href="./exp/finetuning/qa_anet/b16_17m.sh">script</a></td>
        <td><a href="./exp/finetuning/qa_anet/b16_25m.sh">script</a><a href="https://pjlab-gvm-data.oss-cn-shanghai.aliyuncs.com/umt/multi_modality/qa_qnet_b16_25m.pth"> <b>[ckpt]</b></a></td>
        <td><a href="./exp/finetuning/qa_anet/l16_5m.sh">script</a></td>
        <td><a href="./exp/finetuning/qa_anet/l16_17m.sh">script</a></td>
        <td><a href="./exp/finetuning/qa_anet/l16_25m.sh">script</a><a href="https://pjlab-gvm-data.oss-cn-shanghai.aliyuncs.com/umt/multi_modality/qa_qnet_l16_25m.pth"> <b>[ckpt]</b></a></td>
    </tr>
    <tr align="center">
        <th rowspan="2">MSRVTT-QA</th>
        <td>44.3</td>
        <td>44.9</td>
        <td>44.9</td>
        <td>45.5</td>
        <td>46.4</td>
        <td>47.1</td>
    </tr>
    <tr align="center">
        <td><a href="./exp/finetuning/qa_msrvtt/b16_5m.sh">script</a></td>
        <td><a href="./exp/finetuning/qa_msrvtt/b16_17m.sh">script</a></td>
        <td><a href="./exp/finetuning/qa_msrvtt/b16_25m.sh">script</a><a href="https://pjlab-gvm-data.oss-cn-shanghai.aliyuncs.com/umt/multi_modality/qa_msrvtt_b16_25m.pth"> <b>[ckpt]</b></a></td>
        <td><a href="./exp/finetuning/qa_msrvtt/l16_5m.sh">script</a></td>
        <td><a href="./exp/finetuning/qa_msrvtt/l16_17m.sh">script</a></td>
        <td><a href="./exp/finetuning/qa_msrvtt/l16_25m.sh">script</a><a href="https://pjlab-gvm-data.oss-cn-shanghai.aliyuncs.com/umt/multi_modality/qa_msrvtt_l16_25m.pth"> <b>[ckpt]</b></a></td>
    </tr>
    <tr align="center">
        <th rowspan="2">MSRVTT-MC</th>
        <td>95.9</td>
        <td>96.3</td>
        <td>96.3</td>
        <td>96.8</td>
        <td>97.7</td>
        <td>97.3</td>
    </tr>
    <tr align="center">
        <td><a href="./exp/finetuning/mc_msrvtt/b16_5m.sh">script</a></td>
        <td><a href="./exp/finetuning/mc_msrvtt/b16_17m.sh">script</a></td>
        <td><a href="./exp/finetuning/mc_msrvtt/b16_25m.sh">script</a></td>
        <td><a href="./exp/finetuning/mc_msrvtt/l16_5m.sh">script</a></td>
        <td><a href="./exp/finetuning/mc_msrvtt/l16_17m.sh">script</a></td>
        <td><a href="./exp/finetuning/mc_msrvtt/l16_25m.sh">script</a></td>
    </tr>
    <tr align="center">
        <th rowspan="2">MSVD-QA</th>
        <td>49.1</td>
        <td>48.9</td>
        <td>49.5</td>
        <td>51.3</td>
        <td>53.4</td>
        <td>55.2</td>
    </tr>
    <tr align="center">
        <td><a href="./exp/finetuning/qa_msvd/b16_5m.sh">script</a></td>
        <td><a href="./exp/finetuning/qa_msvd/b16_17m.sh">script</a></td>
        <td><a href="./exp/finetuning/qa_msvd/b16_25m.sh">script</a><a href="https://pjlab-gvm-data.oss-cn-shanghai.aliyuncs.com/umt/multi_modality/qa_msvd_b16_25m.pth"> <b>[ckpt]</b></a></td>
        <td><a href="./exp/finetuning/qa_msvd/l16_5m.sh">script</a></td>
        <td><a href="./exp/finetuning/qa_msvd/l16_17m.sh">script</a></td>
        <td><a href="./exp/finetuning/qa_msvd/l16_25m.sh">script</a><a href="https://pjlab-gvm-data.oss-cn-shanghai.aliyuncs.com/umt/multi_modality/qa_msvd_b16_25m.pth"> <b>[ckpt]</b></a></td>
    </tr>
</table>
<br>
</div>