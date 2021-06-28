"""FDR Correction on .nii.gz file"""
import os
import nibabel as nib
import numpy as np
from statsmodels.stats.multitest import multipletests

# Set up
PROJECT_ROOT = "/home/vgonzenb/ISLA/"
mask = nib.load(PROJECT_ROOT + "data/templates/pnc_template_brain_mask_2mm.nii.gz")

cbf_methods =  {'orig': "orig_cbf_th10",
                    'isla_r2': "isla_cbf_r2_th10", 
                    'isla_r3': "isla_cbf_r3_th10", 
                    'isla_r4': "isla_cbf_r4_th10", 
                    'ahlgren_r2': "ahlgren_cbf_r2_th10", 
                    'ahlgren_r3': "ahlgren_cbf_r3_th10", 
                    'ahlgren_r4': "ahlgren_cbf_r4_th10"
                    }
def find_cbf_path(img_key):
    """Find image path per dict key"""
    filepath = PROJECT_ROOT + f"data/stats/{cbf_methods[img_key]}/_vox_p_fstat1.nii.gz"
    return(filepath)

def multipletests_mod(p_values, ret=1, **kwargs):
    """Select what to return from multipletest"""
    result = multipletests(p_values, **kwargs)[ret]
    return result

def nifti_func_wrapper(nifti, func, **kwargs):
    """Wraps functions to work on in-brain voxels of nifti image"""
    if(type(nifti) == str): # if input is a path load img
        nifti = nib.load(nifti) 
    
    arr = nifti.get_fdata()
    dims = arr.shape

    all_values = arr.ravel()
    where_0 = all_values == 0
    brain_values = all_values[np.logical_not(where_0)]

    result = func(brain_values, **kwargs)
    all_values[np.logical_not(where_0)] = result

    arr_new = np.reshape(all_values, dims)
    nifti_new = nib.Nifti1Image(arr_new, nifti.affine) 

    return(nifti_new)