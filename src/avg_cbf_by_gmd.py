"""Create DataFrame with average CBF values per GMD threshold for plotting"""
import nibabel as nib
import numpy as np
import pandas as pd

PROJECT_ROOT = "/home/vgonzenb/ISLA/"
PNC_TEMPLATE = PROJECT_ROOT + 'data/templates/pnc_template_brain_2mm.nii.gz'
subject_list = list(pd.read_csv("/project/kristin_imco/subject_lists/n1132_linnCoupling_ltnT1AslVox_subjects.csv")["scanid"])

def load_images(subjectID, CBF_TYPE):
    """Returns a dictionary of paths"""
    if CBF_TYPE == "CBF":
        cbf_path = f'/project/pnc/n1601_dataFreeze2016/neuroimaging/asl/voxelwiseMaps_cbf/{subjectID}_asl_quant_ssT1Std.nii.gz'
    elif CBF_TYPE == "ISLA":
        cbf_path = f'/project/kristin_imco/coupling_maps_gm10/gmd_cbf_size3/{subjectID}/predictedGMD1.nii.gz'
    elif CBF_TYPE == "Ahlgren":
        cbf_path = f'/project/kristin_imco/coupling_ahlgren_gm10/gmd_cbf_size3/{subjectID}/beta_gmd.nii.gz'
    
    cbf_img = nib.load(cbf_path)

    gmd_path = f"/project/pnc/n1601_dataFreeze2016/neuroimaging/t1struct/voxelwiseMaps_gmd/{subjectID}_atropos3class_prob02SubjToTemp2mm.nii.gz"
    gmd_img = nib.load(gmd_path)

    images = {'cbf_img': cbf_img, 'gmd_img': gmd_img}
    return(images)

def threshold_by_gmd(images):
    cbf_arr, gmd_arr = map(lambda img: np.squeeze(np.where(img.get_fdata() > 0, img.get_fdata(), np.nan)), images.values())

    avg_within_range = []
    for lower_thr in np.linspace(0.1, 0.9, 9):
        upper_thr = lower_thr + 0.1
        mask = np.where(np.logical_and(gmd_arr >= lower_thr, gmd_arr < upper_thr), 1, np.nan)

        avg = np.nanmean(cbf_arr * mask)

        avg_within_range.append(avg)
    return(avg_within_range)

def make_avg_data(CBF_TYPE):
    images = [load_images(subj, CBF_TYPE) for subj in subject_list] 
    avg_cbf = [threshold_by_gmd(img) for img in images]
    df = pd.DataFrame(avg_cbf)
    df.columns = [str(int(t*100)) + "-" + str(int((t + 0.1) * 100)) + "%" for t in np.linspace(0.1, 0.9, 9)]
    df.insert(0, "subjectID", subject_list)
    df.to_csv(PROJECT_ROOT + f'avg_{CBF_TYPE}_per_GMD.csv')
    return(df)

CBF_TYPES = ["CBF", "ISLA", "Ahlgren"]
for type in CBF_TYPES:
    make_avg_data(type)




