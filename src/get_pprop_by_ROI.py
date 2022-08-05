""" Calculate Proportion of signifiscant voxels within ROIs for CBF methods"""
import os
import nibabel as nib
import numpy as np
import pandas as pd
from multitest_nifti import * # custom script

PROJECT_ROOT = os.path.join(os.path.dirname(__file__),'..')
os.chdir(PROJECT_ROOT)
JLF_DIR = "/project/pnc/n1601_dataFreeze2016/neuroimaging/pncTemplate/jlf"
roi_dict_path = os.path.join(JLF_DIR, "jlf_lookup.csv")

roi_labels_path = os.path.join(JLF_DIR, "pncTemplateJLF_Labels2mm.nii.gz")
roi_labels = nib.load(roi_labels_path).get_fdata()
roi_indexes = np.unique(roi_labels)[1:]

p_thresh = 0.05

def make_df():
    """Make DataFrame where columns = proportion of significant tests in ROIs; rows = CBF method"""
    column_names = ["X" + str(int(ROI)) for ROI in roi_indexes]
    df = pd.DataFrame(columns = column_names, index=cbf_methods.keys())
    return(df)

def add_img_row(method_key, adj4thresh=False):
    """Add row to the dataframe by loading, inverting and correcting p-value img"""
    p_img = nib.load(find_cbf_path(method_key))
        
    p_img_inv = nifti_func_wrapper(p_img, lambda p: 1-p)
    p_img_corr = nifti_func_wrapper(p_img_inv, multipletests_mod, method = 'fdr_bh')
    p_arr_corr = p_img_corr.get_fdata()

    if(adj4thresh):
        thresh_mask = np.where(p_img.get_fdata() > 0, 1, 0) # where p_img = 0: out of 10% gmd threshold

    p_propor = []
    for roi_index in roi_indexes:
        roi_mask  = roi_labels == roi_index
        if(adj4thresh): # apply mask to the roi mask
            roi_mask = roi_mask * thresh_mask
        nvox_roi = np.sum(roi_mask)

        sig_vox_roi = np.where(roi_mask, p_arr_corr <= p_thresh, 0)
        
        p_propor.append(np.sum(sig_vox_roi) / nvox_roi)

    return p_propor

if __name__ == '__main__':
    df = make_df()
    for adj in False, True:
        df = make_df()
        for method in cbf_methods:
            df.loc[method] = add_img_row(method)
        
        
        outname = f"results/data/prop_sigPs_by_ROI{'adjBy10thr' if adj else ''}.csv"
        df.to_csv(outname)