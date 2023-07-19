# Dataset Preparation

## Action Recognition

We follow [UniFormerV2](https://github.com/OpenGVLab/UniFormerV2/) to prepare the datasets. All the data files can be found [here](https://drive.google.com/drive/folders/17VB-XdF3Kfr9ORmnGyXCxTMs86n0L4QL?usp=sharing), including:
- [Kinetics-400/600/700](https://www.deepmind.com/open-source/kinetics)
- [Kinetics-710](https://github.com/OpenGVLab/UniFormerV2/blob/main/DATASET.md)
- [Moments in Time V1](http://moments.csail.mit.edu/)
- [Something-Something V1&V2](https://developer.qualcomm.com/software/ai-datasets/something-something)

Since some videos in Kinetics may no longer be available, it will lead to small performance gap. Our version of Kinetics-400 can be downloaded via **[Baidu Cloud](https://pan.baidu.com/s/150AE6OK9GjWQQvXv_db8vw) (password: li0f)**


## Action Detection

The pre-processing of **AVA v2.2** can be summarized into 2 steps:

  1. Download the processed dataset from [Google Drive](https://drive.google.com/file/d/1lqDuz3zaP-wma3QbexDxtWW6stza5YFZ) or [Baidu NetDisk](https://pan.baidu.com/s/1UrflK4IgiVbVBOP5fDHdKA) (password: q5v5).

  2. run following commands to unzip the file and create a symbolic link to the extracted files.
     ```
     tar zxvf AVA_compress.tar.gz -C your_data_path
     cd single_modality/action_detection
     ln -s your_data_path/AVA data/AVA
     ```

As for the step-by-step preparation, please follow the instructions in [AlphAction](https://github.com/MVIG-SJTU/AlphAction/blob/master/DATA.md#step-by-step-version) for step-by-step data preparation.
