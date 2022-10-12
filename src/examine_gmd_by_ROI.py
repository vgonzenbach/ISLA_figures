"""For each ROI, calculate proportion of ROI voxels remaining after 10% GMD thresholding"""
import os
import nibabel as nib
import numpy as np
import pandas as pd # custom script

PROJECT_ROOT = os.path.join(os.path.dirname(__file__),'..')
os.chdir(PROJECT_ROOT)
JLF_DIR = "/project/pnc/n1601_dataFreeze2016/neuroimaging/pncTemplate/jlf/"
roi_dict = pd.read_excel('data/MUSE_ROI_Dict.xlsx')
roi_labels = nib.load(JLF_DIR + "pncTemplateJLF_Labels2mm.nii.gz").get_fdata()
roi_indices = np.unique(roi_labels)[1:] # excluded 0 = background

gmd_path = '/project/kristin_imco/avg_images/avgGMD_CBF_thr10.nii.gz'
gmd_arr = nib.load(gmd_path).get_fdata()

def get_total_voxels(roi):
    roi_mask = np.where(roi_labels == roi, 1, 0)
    n_total_voxels = np.sum(roi_mask)
    return n_total_voxels

def get_propvox_included(roi):
    roi_mask = np.where(roi_labels == roi, 1, 0)
    n_total_voxels = get_total_voxels(roi)
    n_included_voxels = np.sum(np.where(roi_mask, gmd_arr > .1, 0))
    return n_included_voxels / n_total_voxels

def get_avg_gmd(roi):
    roi_mask = np.where(roi_labels == roi, True, False)
    gmd_masked = gmd_arr * roi_mask
    avg_gmd = np.mean(gmd_masked, where=np.where(gmd_arr * roi_mask != 0, True, False))
    return avg_gmd

df = pd.DataFrame(index = ["X" + str(int(ROI)) for ROI in roi_indices])
df["AVG_GMD"] = [get_avg_gmd(roi) for roi in roi_indices]
df["NVOX"] = [get_total_voxels(roi) for roi in roi_indices]
df["PROP_VOX_ABV10%"] = [get_propvox_included(roi) for roi in roi_indices]
df.to_csv('results/data/roi_gmd.csv')

