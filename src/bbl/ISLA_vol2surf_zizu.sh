#!/bin/bash
source /Applications/freesurfer/7.1.1/SetUpFreeSurfer.sh

export ISLA_IMG=/Users/vgonzenb/PennSIVE/ISLA/data/avg_images/avgISLA/avgISLA_cbf_size2_thr10.nii.gz
mri_vol2surf --mov isla2mni.nii.gz \
  --mni152reg \
  --o ./rh.avgISLA_cbf_size2_thr10.mgh \
  --interp trilinear --noreshape \
  --hemi rh \
  --projfrac 0.5 \
  --trgsubject fsaverage


#OR

mri_vol2surf --mov isla2mni.nii.gz  --hemi lh --surf white \
--reg $FREESURFER_HOME/average/mni152.register.dat \
--projfrac-avg 0 1 0.1 --o newsurf.mgh

  mri_surf2surf --srcsubject pnc_template  \
		--trgsubject fsaverage --trgicoorder 5 --hemi rh \
		--srcsurfval rh.avgISLA_cbf_size2_thr10.mgh  \
		--trgsurfval newsurf.mgh
