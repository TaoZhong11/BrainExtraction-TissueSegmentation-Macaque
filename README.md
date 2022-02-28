# BrainExtraction-TissueSegmentation-Macaque
Trained on large scale macaque brain data-set.

Parts of codes are borrowed from [nn-UNet](https://github.com/MIC-DKFZ/nnUNet) and [nn-Former](https://github.com/282857341/nnFormer)

---
## Installation
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

---

## Training
Please see nnFormer documents.


---
## Pretrained models
Unzip the downloaded pre-training models.
the download link is 
```
Link：https://pan.baidu.com/s/14w_uiQtq38bYjkyeDvWNnw 
code：smu1
```


## Inference for Brain Extraction
```
nnFormer_predict -i nnFormer_raw_data_base/nnFormer_raw_data/Task505_ss/imagesTs  -o  OUTPUT_PATH  -m  3d_fullres    -t  505  -chk model_best  -f  0/1/2/3
```

## Inference for Tissue Segmentation
```
nnFormer_predict -i nnFormer_raw_data_base/nnFormer_raw_data/Task504_2macaque/imagesTs  -o  OUTPUT_PATH  -m  3d_fullres    -t  504  -chk model_best  -f  0/1/2/3
```


