#!/bin/bash

file_name="$1"
export TRANSFORM_DIR=$PWD/data/transforms 
export CBF_PNC=$PWD/data/mri/$file_name
export CBF_MNI=$PWD/data/mri/reg/$file_name

antsApplyTransforms -i $CBF_PNC -o $CBF_MNI -t $TRANSFORM_DIR/PNC-MNI_0warp.nii.gz -t $TRANSFORM_DIR/PNC-MNI_1Affine.mat \
    -r $PWD/data/templates/MNI-2x2x2.nii.gz -d 3 -e 3 -n LanczosWindowedSinc
echo "Transform complete "
