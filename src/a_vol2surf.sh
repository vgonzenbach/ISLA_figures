# 1. initialize FreeSurfer
export FREESURFER_HOME=/Applications/freesurfer/7.1.1  # edit path
source $FREESURFER_HOME/SetUpFreeSurfer.sh

# 2. run recon-all (commented out)
export SUBJECTS_DIR=$FREESURFER_HOME/subjects # edit path
#recon-all -i data/template/pnc_template.nii.gz -s pnc_template -all

# 3. project to surface 
export CBF_IMG=/Users/vgonzenb/PennSIVE/ISLA/data/mri/avgCBF_thr10.nii.gz # edit path
export CBF_SURF=/Users/vgonzenb/PennSIVE/ISLA/data/surf/a_lh.${CBF_IMG:39:12}.mgz # edit ouput path (does not exist at runtime)

mri_vol2surf --mov $CBF_IMG \
  --regheader pnc_template \
  --o $CBF_SURF \
  --hemi lh \
  --trgsubject fsaverage

# 4. view results
freeview  -f $SUBJECTS_DIR/fsaverage/surf/lh.inflated::overlay=$CBF_SURF:overlay_method=piecewise:overlay_threshold=20,55,90 \
--viewport 3d