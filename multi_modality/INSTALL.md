# Installation

## Requirements

We mainly follow [VINDLU](https://github.com/klauscc/VindLU/) to prepare the enviroment.

```shell
# create 
conda env create -f vl.yml
# activate
conda activate vl
```

## Note

To run UMT pretraining, you have to prepare the weights of the **CLIP visual encoder** as in the [extract.ipynb](../single_modality/models/extract_clip/extract.ipynb), and set the `MODEL_PATH` in [clip.py](./models/backbones/vit/clip.py).