# Installation

## Requirements

We mainly follow [VideoMAE](https://github.com/MCG-NJU/VideoMAE) to prepare the enviroment.

```shell
pip install -r requirements.txt
```

We follow VideoMAE to set `--epochs 201` to avoid the potential interrupt in the last epoch.

> We observed accidental interrupt in the last epoch when conducted the pre-training experiments on V100 GPUs (PyTorch 1.6.0). This interrupt is caused by the scheduler of learning rate. We naively set --epochs 801 to walk away from issue.

## Note

To run UMT pretraining, you have to prepare the weights of the **CLIP visual encoder** as in the [extract.ipynb](./models/extract_clip/extract.ipynb), and set the `MODEL_PATH` in [clip.py](./models/clip.py).