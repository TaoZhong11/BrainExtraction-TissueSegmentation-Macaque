## BETS_Formers: Brain Extraction and Tissue Segmentation for Macaque using Transformer Models
Trained on large scale macaque brain data-set from different sites.

Parts of codes are borrowed from [nn-UNet](https://github.com/MIC-DKFZ/nnUNet) and [nn-Former](https://github.com/282857341/nnFormer)

Previous works on macaque MRI:
```
Tao Zhong, Fenqiang Zhao, Yuchen Pei, Zhenyuan Ning, Lufan Liao, Zhengwang Wu, Yuyu Niu, Li Wang, Dinggang Shen, Yu Zhang, Gang Li. 
DIKA-Nets: Domain-invariant knowledge-guided attention networks for brain skull stripping of early developing macaques. Neuroimage, 2021, 227: 117649. 

Tao Zhong, Jingkuan Wei, Kunhua Wu, Liangjun Chen, Fenqiang Zhao, Yuchen Pei, Ya Wang, Hongjiang Zhang, Zhengwang Wu, Ying Huang, Tengfei Li, Li Wang, Yongchang Chen, Weizhi Ji, Yu Zhang, Gang Li, Yuyu Niu. 
Longitudinal Brain Atlases for Early Developing Cynomolgus Macaques from Birth to 48 Months of Age. Neuroimage, 2022, 247: 118799.
```
---
## Docker (Highly recommended)
#### 1、Pull
The docker image has been uploaded onto DockerHub, download it by using the following command
```
docker pull wxyabc/bets_formers:1.0
docker run -it --gpus=all --ipc=host --name "NAME" wxyabc/bets_formers:1.0 /bin/bash
```
#### 2、Inference
Follow the inference instruction in the bottom for brain extraction and tissue segmentation.

## Installation (If you don't use docker)
#### 1、System requirements
This software was originally designed and run on a system running Ubuntu 18.01, with Python 3.6, PyTorch 1.8.1, and CUDA 10.1. For a full list of software packages and version numbers, see the Conda environment file `environment.yml`. 

This software leverages graphical processing units (GPUs) to accelerate neural network training and evaluation; systems lacking a suitable GPU will likely take an extremely long time to train or evaluate models. The software was tested with the NVIDIA RTX 2080 TI GPU, though we anticipate that other GPUs will also work, provided that the unit offers sufficient memory. 

#### 2、Installation guide

We recommend installation of the required packages using the Conda package manager, available through the Anaconda Python distribution. Anaconda is available free of charge for non-commercial use through [Anaconda Inc](https://www.anaconda.com/products/individual). After installing Anaconda and cloning this repository, For use as integrative framework：
```
conda env create -f environment.yml
source activate Macaque_Transformers
pip install -e .
```

#### 3、Set environment variables

The models need to know where you intend to save raw data and trained models. For this you need to set a few of environment variables：
```
gedit ~/.bashrc
```
Once the file is open in a text editor, add the following lines to the bottom:
```
export nnFormer_raw_data_base="xxx/xxx/xxx/nnFormer_raw_data_base"
export nnFormer_raw_data="xxx/xxx/xxx/nnFormer_raw_data_base/nnFormer_raw_data"
export RESULTS_FOLDER_nnFormer="xxx/xxx/xxx/nnFormer_trained_models"
```
#### 4、 Pretrained models
Unzip the downloaded pre-training models.
the download link is 
```
Link：https://pan.baidu.com/s/14w_uiQtq38bYjkyeDvWNnw 
code：smu1
```
---

## Inference for Brain Extraction
This model intends to obtain a brain mask from macaque T1w MRI.
The inference subject should be located in nnFormer_raw_data_base/nnFormer_raw_data/Task505_ss/imagesTs as "AAAAAA(DATASET_NAME)_BBB(SUBJECT_ID)_CCCC(MODALITY)".
Now this version only supports T1w modality. So the example file name can be "Cynomolgus_001_0000.nii.gz". We have upload 3 subjects from different sites as examples. For more macaque data please see [PRIMatE-DE](http://fcon_1000.projects.nitrc.org/indi/PRIMEdownloads.html).

```
nnFormer_predict -i nnFormer_raw_data_base/nnFormer_raw_data/Task505_ss/imagesTs  -o  505_brain_mask  -m  3d_fullres    -t  505  -chk model_best  (-f 0/1/2/3/4 if you need to specify model)
```
Brain mask can be generated in this step. Check the brain mask and manually correct it if necessary. Then it can be used to extract macaque brain images (from with-skull images) for tissue segmentation:
```
python extract_brain_by_505.py
```
## Inference for Tissue Segmentation
This model would output 4 class label maps, including WM, GM, CSF, and Cerebellum&Brainstem.
```
nnFormer_predict -i nnFormer_raw_data_base/nnFormer_raw_data/Task504_2macaque/imagesTs  -o  OUTPUT_PATH  -m  3d_fullres    -t  504  -chk model_best  (-f 0/1/2/3/4 if you need to specify model)
```
---
## Training
Please see [nn-UNet](https://github.com/MIC-DKFZ/nnUNet) and [nn-Former](https://github.com/282857341/nnFormer).




