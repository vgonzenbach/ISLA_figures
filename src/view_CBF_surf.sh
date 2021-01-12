source /Applications/freesurfer/7.1.1/SetUpFreeSurfer.sh
export CBF_SURF_L=/Users/vgonzenb/PennSIVE/ISLA/output_mri2vol/lh.avgCBF_thr10_old.mgz
export CBF_SURF_R=/Users/vgonzenb/PennSIVE/ISLA/output_mri2vol/rh.avgCBF_thr10_old.mgz

freeview  -f $SUBJECTS_DIR/fsaverage/surf/lh.inflated::overlay=$CBF_SURF_L:overlay_method=piecewise:overlay_threshold=20,55,90 \
$SUBJECTS_DIR/fsaverage/~surf/rh.inflated:overlay_method=linear:overlay_threshold=0,87:overlay=$CBF_SURF_R \
--viewport 3d
