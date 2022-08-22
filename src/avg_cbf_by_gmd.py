"""Create DataFrame with average CBF values per GMD threshold for plotting"""
import os
import nibabel as nib
import numpy as np
import pandas as pd

PROJECT_ROOT = os.path.join(os.path.dirname(__file__),'..')
os.chdir(PROJECT_ROOT)
PNC_TEMPLATE = 'data/templates/pnc_template_brain_2mm.nii.gz'
subject_list = list(pd.read_csv("/project/kristin_imco/subject_lists/n1132_linnCoupling_ltnT1AslVox_subjects.csv")["scanid"])

def load_images(subjectID, size):
    """Returns a hierarchical dictionary containing CBF and GMD arrays from images for a given subject and size"""

    images = {}
    images['subjectID'] = subjectID
    images['gmd'] = nib.load(f"/project/pnc/n1601_dataFreeze2016/neuroimaging/t1struct/voxelwiseMaps_gmd/{subjectID}_atropos3class_prob02SubjToTemp2mm.nii.gz").get_fdata()
    images['cbf'] = {}
    images['cbf']['Raw'] = nib.load(f'/project/pnc/n1601_dataFreeze2016/neuroimaging/asl/voxelwiseMaps_cbf/{subjectID}_asl_quant_ssT1Std.nii.gz').get_fdata()
    images['cbf']['ISLA'] = nib.load(f'/project/kristin_imco/coupling_maps_gm10/gmd_cbf_size{size}/{subjectID}/predictedGMD1.nii.gz').get_fdata()
    images['cbf']['Ahlgren'] = nib.load(f'/project/kristin_imco/coupling_ahlgren_gm10/gmd_cbf_size{size}/{subjectID}/beta_gmd.nii.gz').get_fdata()
    try: 
        images['cbf']['BASIL'] = nib.load(f'/project/pnc/basilPNC_scanid/{subjectID}_basil.nii.gz').get_fdata()
    except FileNotFoundError:
        images['cbf']['BASIL'] = np.nan

    return(images)

def threshold_cbf(images):
    """Thresholds and averages each CBF image"""

    def make_gmd_masks(images):
        """Return DataFrame where rows represent avg values in GMD threshold for all three CBF types"""
    
        gmd_arr = images['gmd']
        lower_thr = np.linspace(0.1, 0.9, 9)
        upper_thr = lower_thr + .1

        # Get GMD-based mask for each 10% interval in GMD
        gmd_masks = [] 
        for lower_th, upper_th in zip(lower_thr, upper_thr):
            gmd_mask = np.where(np.logical_and(gmd_arr >= lower_th, gmd_arr < upper_th), 1, np.nan)   
            gmd_masks.append(gmd_mask)
        return(gmd_masks)

    masks = make_gmd_masks(images)
    df_rows = []
    for cbf_type in images['cbf']:
        row = [images['subjectID'], cbf_type]

        pre_cbf_arr = images['cbf'][cbf_type]
        cbf_arr = np.squeeze(np.where(pre_cbf_arr > 0, pre_cbf_arr, np.nan)) # take care of faulty negative values
        avg_cbf_values = [np.nanmean(cbf_arr * mask) for mask in masks]
        row.extend(avg_cbf_values)
        df_rows.append(row)
    
    return(df_rows)

def make_avg_cbf_df(size):
    """Wrapper: Returns a single DataFrame aggregating results from 'threshold_cbf' for all subjects"""
    
    list4df = []
    for subject in subject_list:
        images = load_images(subject, size)
        rows = threshold_cbf(images)
        list4df.extend(rows)

    # Name columns
    avg_cbf_df = pd.DataFrame.from_records(list4df)
    colnames = ['subjectID', 'method']
    colnames.extend([str(int(t*100)) + "-" + str(int((t + 0.1) * 100)) + "%" for t in np.linspace(0.1, 0.9, 9)])
    avg_cbf_df.columns = colnames
    return(avg_cbf_df)

    # return(list4df)

if __name__ == '__main__':
    outdir = 'results/data'
    if not os.path.exists(outdir):
        os.makedirs(outdir)

    for r_size in 2, 3, 4: # Radius sizes
        cbf_df = make_avg_cbf_df(r_size)
        outpath = os.path.join(outdir, f'avg_cbf_vals_by_GMD_size-{r_size}.csv')
        cbf_df.to_csv(outpath, index=False)





