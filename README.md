# Brain-Extrain-and-Tissue-Segmentation-Transformer-Models-for-Macaque
They are trained on large-scale macaque brain data-set.
The models were built on nnFormer (https://github.com/282857341/nnFormer) and nnUnet (https://github.com/MIC-DKFZ/nnUNet).
For installation please see nnFormer.

Task504 was built for brain extraction.
Task505 was built for tissue segmentation.

Both tasks were built on a 5-fold strategy and, therefore, 5 models for each task. You can use the ensemble strategy by all models in each task.

For brain extraction, setting up the T1w data as nnFormer_raw_data_base/nnFormer_raw_data/Task504_2macaque/imagesTs/macaque_xxx_0000.nii.gz

Then run: nnFormer_predict -i INPUT_FOLDER -o OUTPUT_FOLDER -t 504 -m 3d_fullres

Tissue segmentation is similar except for the task ID change to 505.
