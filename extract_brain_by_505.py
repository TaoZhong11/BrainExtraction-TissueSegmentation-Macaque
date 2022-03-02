import os
import SimpleITK as sitk
import numpy as np



T1_path = 'nnFormer_raw_data_base/nnFormer_raw_data/Task505_ss/imagesTs'
# T2_path = '../data//T2/'
Seg_path = '505_brain_mask/'


files = os.listdir(T1_path)
output_path = 'nnFormer_raw_data_base/nnFormer_raw_data/Task504_2macaque/imagesTs'
subjects = []

for subject in files:
    T1_name = subject
    seg_name = subject[0:-12]

    print(T1_name,seg_name)
    
    T1_img = sitk.ReadImage(T1_path + T1_name)
    Seg_img = sitk.ReadImage(Seg_path + seg_name)
    
    T1_array = sitk.GetArrayFromImage(T1_img)
    Seg_array = sitk.GetArrayFromImage(Seg_img)
    
    output_array = T1_array*Seg_array
    output_array = output_array.astype(np.int16)
    output_img  = sitk.GetImageFromArray(output_array)
    sitk.WriteImage(output_img, output_path + T1_name)

    
    
    
    
    
    
