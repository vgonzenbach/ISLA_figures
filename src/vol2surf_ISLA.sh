#!/bin/bash
source /Applications/freesurfer/7.1.1/SetUpFreeSurfer.sh

export ISLA_DIR=/Users/vgonzenb/PennSIVE/ISLA/data/avg_images/avgISLA
for ISLA_IMG in $ISLA_DIR/*size3_thr10.nii.gz
do
  mri_vol2surf --mov $ISLA_IMG \
  --regheader pnc_template \
  --o ./output_mri2vol/rh.${ISLA_IMG:54:23}.mgz \
  --hemi rh \
  --trgsubject fsaverage

  mri_vol2surf --mov $ISLA_IMG \
  --regheader pnc_template \
  --o ./output_mri2vol/lh.${ISLA_IMG:54:23}.mgz \
  --hemi lh \
  --trgsubject fsaverage
done
