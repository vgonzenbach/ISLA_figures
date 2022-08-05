"""FDR Correction on .nii.gz file"""
import os
import nibabel as nib
import numpy as np
from statsmodels.stats.multitest import multipletests

# Set up
PROJECT_ROOT = os.path.join(os.path.dirname(__file__),'..')
mask_path = os.path.join('/project/pnc/n1601_dataFreeze2016/neuroimaging/pncTemplate/pnc_template_brain_mask_2mm.nii.gz')
mask = nib.load(mask_path)

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
    filepath = f"/project/kristin_imco/flameo_final/cbf/nogmd/{cbf_methods[img_key]}/randomize/_vox_p_fstat1.nii.gz"
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