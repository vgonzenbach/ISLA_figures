# Surface Projection in PNC space

# 1. init FreeSurfer
export FREESURFER_HOME=/Applications/freesurfer/7.1.1  # edit path
source $FREESURFER_HOME/SetUpFreeSurfer.sh

# 2. run recon-all (commented out)
export SUBJECTS_DIR=$FREESURFER_HOME/subjects # edit path
#recon-all -i data/template/pnc_template.nii.gz -s pnc_template -all

# 3. register brain to pnc_template
export SUBJECTS_DIR=$FREESURFER_HOME/subjects # edit path
export PNC_BRAIN=data/template/pnc_template_brain.nii.gz # edit path
export TRANSFORM=data/transform/identity.dat # edit path

fslregister --s pnc_template --mov $PNC_BRAIN --reg $TRANSFORM

# 4. project to surface
export CBF_IMG=/Users/vgonzenb/PennSIVE/ISLA/data/mri/avgCBF_thr10.nii.gz # edit path 
export CBF_SURF=/Users/vgonzenb/PennSIVE/ISLA/data/surf/c_lh.${CBF_IMG:39:12}.mgz # edit ouput path (does not exist at runtime)

mri_vol2surf --mov $CBF_IMG \
--reg $TRANSFORM \
--o $CBF_SURF \
--hemi lh \
--trgsubject pnc_template

# 4. visualize surface
freeview  -f $SUBJECTS_DIR/pnc_template/surf/lh.inflated::overlay=$CBF_SURF:overlay_method=piecewise:overlay_threshold=20,55,90 \
--viewport 3d 