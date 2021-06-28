"""For each ROI, calculate proportion of ROI voxels remaining after 10% GMD thresholding"""

import nibabel as nib
import numpy as np
import pandas as pd # custom script

PROJECT_ROOT = "/home/vgonzenb/ISLA/"
JLF_DIR = "/project/pnc/n1601_dataFreeze2016/neuroimaging/pncTemplate/jlf/"
roi_labels_path = JLF_DIR + "pncTemplateJLF_Labels2mm.nii.gz"
roi_dict_path = JLF_DIR + "jlf_lookup.csv"

roi_labels_img = nib.load(roi_labels_path)
roi_labels_arr = roi_labels_img.get_fdata()
roi_indexes = np.unique(roi_labels_img.get_fdata())[1:]

gmd_path = PROJECT_ROOT + 'data/mri/avgGMD_CBF_thr10.nii.gz'
gmd_img = nib.load(gmd_path)
gmd_arr = gmd_img.get_fdata()

def thresh_rois():
    """Returns proportions of within-threshold voxels for each ROI"""
    inVox_propor = []
    for roi_index in roi_indexes:
        roi_mask  = roi_labels_arr == roi_index
        nvox_roi = np.sum(roi_mask)

        isInThresh = np.where(roi_mask, gmd_arr > .1, 0)
        inVox_propor.append(np.sum(isInThresh) / nvox_roi)
    return inVox_propor


df = pd.DataFrame(index = ["X" + str(int(ROI)) for ROI in roi_indexes], columns=['PROP_VOX_ABV10%'])
df["PROP_VOX_ABV10%"] = thresh_rois()