# Unmasked Teacher

This repo is the official implementation of ["Unmasked Teacher: Towards Training-Efficient Video Foundation Models"](https://arxiv.org/abs/2303.16058).
By [Kunchang Li](https://scholar.google.com/citations?user=D4tLSbsAAAAJ), [Yali Wang](https://scholar.google.com/citations?user=hD948dkAAAAJ), [Yizhuo Li](https://scholar.google.com/citations?user=pyBSGjgAAAAJ), [Yi Wang](https://scholar.google.com.hk/citations?hl=zh-CN&user=Xm2M8UwAAAAJ), [Yinan He](https://dblp.org/pid/93/7763.html), [Limin Wang](https://scholar.google.com/citations?user=HEuN8PcAAAAJ) and [Yu Qiao](https://scholar.google.com/citations?user=gFtI-8QAAAAJ&hl).
![teaser](img/intro.png)

## Update

Code and models will be released soon.

## Introduction

Video Foundation Models (VFMs) have received limited exploration due to high computational costs and data scarcity. Previous VFMs rely on Image Foundation Models (IFMs), which face challenges in transferring to the video domain. Although VideoMAE has trained a robust ViT from limited data, its low-level reconstruction poses convergence difficulties and conflicts with high-level cross-modal alignment. This paper proposes a training-efficient method for temporal-sensitive VFMs that integrates the benefits of existing methods. To increase data efficiency, we mask out most of the low-semantics video tokens, but selectively align the unmasked tokens with IFM, which serves as the UnMasked Teacher (UMT). By providing semantic guidance, our method enables faster convergence and multimodal friendliness. With a progressive pre-training framework, our model can handle various tasks including scene-related, temporal-related, and complex video-language understanding. Using only public sources for pre-training in 6 days on 32 A100 GPUs, our scratch-built ViT-L/16 achieves state-of-the-art performances on various video tasks.
![teaser](img/framework.png)


[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/unmasked-teacher-towards-training-efficient/action-classification-on-kinetics-400)](https://paperswithcode.com/sota/action-classification-on-kinetics-400?p=unmasked-teacher-towards-training-efficient)
[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/unmasked-teacher-towards-training-efficient/action-classification-on-kinetics-600)](https://paperswithcode.com/sota/action-classification-on-kinetics-600?p=unmasked-teacher-towards-training-efficient)
[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/unmasked-teacher-towards-training-efficient/action-classification-on-kinetics-700)](https://paperswithcode.com/sota/action-classification-on-kinetics-700?p=unmasked-teacher-towards-training-efficient)	
[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/unmasked-teacher-towards-training-efficient/action-classification-on-moments-in-time)](https://paperswithcode.com/sota/action-classification-on-moments-in-time?p=unmasked-teacher-towards-training-efficient)
[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/unmasked-teacher-towards-training-efficient/action-recognition-on-ava-v2-2)](https://paperswithcode.com/sota/action-recognition-on-ava-v2-2?p=unmasked-teacher-towards-training-efficient)
[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/unmasked-teacher-towards-training-efficient/video-retrieval-on-activitynet)](https://paperswithcode.com/sota/video-retrieval-on-activitynet?p=unmasked-teacher-towards-training-efficient)
[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/unmasked-teacher-towards-training-efficient/video-retrieval-on-didemo)](https://paperswithcode.com/sota/video-retrieval-on-didemo?p=unmasked-teacher-towards-training-efficient)
[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/unmasked-teacher-towards-training-efficient/video-retrieval-on-lsmdc)](https://paperswithcode.com/sota/video-retrieval-on-lsmdc?p=unmasked-teacher-towards-training-efficient)
[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/unmasked-teacher-towards-training-efficient/video-retrieval-on-msr-vtt)](https://paperswithcode.com/sota/video-retrieval-on-msr-vtt?p=unmasked-teacher-towards-training-efficient)
[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/unmasked-teacher-towards-training-efficient/video-retrieval-on-msvd)](https://paperswithcode.com/sota/video-retrieval-on-msvd?p=unmasked-teacher-towards-training-efficient)
[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/unmasked-teacher-towards-training-efficient/video-retrieval-on-ssv2-label-retrieval)](https://paperswithcode.com/sota/video-retrieval-on-ssv2-label-retrieval?p=unmasked-teacher-towards-training-efficient)
[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/unmasked-teacher-towards-training-efficient/video-retrieval-on-ssv2-template-retrieval)](https://paperswithcode.com/sota/video-retrieval-on-ssv2-template-retrieval?p=unmasked-teacher-towards-training-efficient)
[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/unmasked-teacher-towards-training-efficient/zero-shot-video-retrieval-on-activitynet)](https://paperswithcode.com/sota/zero-shot-video-retrieval-on-activitynet?p=unmasked-teacher-towards-training-efficient)
[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/unmasked-teacher-towards-training-efficient/zero-shot-video-retrieval-on-didemo)](https://paperswithcode.com/sota/zero-shot-video-retrieval-on-didemo?p=unmasked-teacher-towards-training-efficient)
[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/unmasked-teacher-towards-training-efficient/zero-shot-video-retrieval-on-lsmdc)](https://paperswithcode.com/sota/zero-shot-video-retrieval-on-lsmdc?p=unmasked-teacher-towards-training-efficient)
[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/unmasked-teacher-towards-training-efficient/zero-shot-video-retrieval-on-msr-vtt)](https://paperswithcode.com/sota/zero-shot-video-retrieval-on-msr-vtt?p=unmasked-teacher-towards-training-efficient)
[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/unmasked-teacher-towards-training-efficient/zero-shot-video-retrieval-on-msvd)](https://paperswithcode.com/sota/zero-shot-video-retrieval-on-msvd?p=unmasked-teacher-towards-training-efficient)
[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/unmasked-teacher-towards-training-efficient/video-question-answering-on-activitynet-qa)](https://paperswithcode.com/sota/video-question-answering-on-activitynet-qa?p=unmasked-teacher-towards-training-efficient)
[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/unmasked-teacher-towards-training-efficient/visual-question-answering-on-msrvtt-qa-1)](https://paperswithcode.com/sota/visual-question-answering-on-msrvtt-qa-1?p=unmasked-teacher-towards-training-efficient)
[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/unmasked-teacher-towards-training-efficient/visual-question-answering-on-msvd-qa-1)](https://paperswithcode.com/sota/visual-question-answering-on-msvd-qa-1?p=unmasked-teacher-towards-training-efficient)


##  Cite

If you find this repository useful, please use the following BibTeX entry for citation.

```latex
@misc{li2023unmasked,
      title={Unmasked Teacher: Towards Training-Efficient Video Foundation Models}, 
      author={Kunchang Li and Yali Wang and Yizhuo Li and Yi Wang and Yinan He and Limin Wang and Yu Qiao},
      year={2023},
      eprint={2303.16058},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}
```