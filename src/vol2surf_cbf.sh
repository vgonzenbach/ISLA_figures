#!/bin/bash
source /Applications/freesurfer/7.1.1/SetUpFreeSurfer.sh

export CBF_IMG=/Users/vgonzenb/PennSIVE/ISLA/data/avg_images/avgCBF_thr10.nii.gz

  mri_vol2surf --mov $CBF_IMG \
  --reg brain.dat \
  --o ./output_mri2vol/rh.avgCBF_thr10.mgz \
  --hemi rh \
  --trgsubject fsaverage

  mri_vol2surf --mov $CBF_IMG \
  --reg brain.dat \
  --o ./output_mri2vol/lh.avgCBF_thr10.mgz \
  --hemi lh \
  --trgsubject fsaverage
