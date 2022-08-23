#!/bin/bash
module load ANTs
cd $(dirname $0)/.. 
TRANSFORM_DIR=$PWD/data/transforms 

for input_img in $(find data/mri -type f -maxdepth 1 | grep -v GMD); do
    output_img=$(dirname $input_img)/reg/$(basename $input_img)
    if [ ! -f $output_img ]; then
        antsApplyTransforms -i $input_img -o $output_img -t $TRANSFORM_DIR/PNC-MNI_0Warp.nii.gz -t $TRANSFORM_DIR/PNC-MNI_1Affine.mat \
            -r $PWD/data/templates/MNI-2x2x2.nii.gz -d 3 -e 3 -n LanczosWindowedSinc
        echo "Transform completed for $input_img"
    fi
done

