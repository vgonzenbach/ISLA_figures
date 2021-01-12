# remember: use fullpath to call `rh.inflated` surface
source /Applications/freesurfer/7.1.1/SetUpFreeSurfer.sh
export R_SIZE_2_THR_10=/Users/vgonzenb/PennSIVE/ISLA/output_mri2vol/rh.avgISLA_cbf_size2_thr10.mgz
export R_SIZE_2_THR_20=/Users/vgonzenb/PennSIVE/ISLA/output_mri2vol/rh.avgISLA_cbf_size2_thr20.mgz
export R_SIZE_3_THR_10=/Users/vgonzenb/PennSIVE/ISLA/output_mri2vol/rh.avgISLA_cbf_size3_thr10.mgz
export R_SIZE_3_THR_20=/Users/vgonzenb/PennSIVE/ISLA/output_mri2vol/rh.avgISLA_cbf_size3_thr20.mgz
export R_SIZE_4_THR_10=/Users/vgonzenb/PennSIVE/ISLA/output_mri2vol/rh.avgISLA_cbf_size4_thr10.mgz
export R_SIZE_4_THR_20=/Users/vgonzenb/PennSIVE/ISLA/output_mri2vol/rh.avgISLA_cbf_size4_thr20.mgz

export L_SIZE_2_THR_10=/Users/vgonzenb/PennSIVE/ISLA/output_mri2vol/lh.avgISLA_cbf_size2_thr10.mgz
export L_SIZE_2_THR_20=/Users/vgonzenb/PennSIVE/ISLA/output_mri2vol/lh.avgISLA_cbf_size2_thr20.mgz
export L_SIZE_3_THR_10=/Users/vgonzenb/PennSIVE/ISLA/output_mri2vol/lh.avgISLA_cbf_size3_thr10.mgz
export L_SIZE_3_THR_20=/Users/vgonzenb/PennSIVE/ISLA/output_mri2vol/lh.avgISLA_cbf_size3_thr20.mgz
export L_SIZE_4_THR_10=/Users/vgonzenb/PennSIVE/ISLA/output_mri2vol/lh.avgISLA_cbf_size4_thr10.mgz
export L_SIZE_4_THR_20=/Users/vgonzenb/PennSIVE/ISLA/output_mri2vol/lh.avgISLA_cbf_size4_thr20.mgz

freeview -f $SUBJECTS_DIR/fsaverage/surf/lh.inflated:overlay_method=linear:overlay_threshold=0,87:overlay=$L_SIZE_3_THR_10 \
--viewport 3d
