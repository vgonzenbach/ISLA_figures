"""Keep editing"""

## 2. Transform w ANTs
export TRANSFORM_DIR=$PWD/data/transforms 
export CBF_PNC=$PWD/data/mri/avgCBF_thr10.nii.gz
export CBF_MNI=$PWD/data/mri/reg/avgCBF_thr10_MNI.nii.gz

antsApplyTransforms -i $CBF_PNC -o $PWD/data/mri/reg/avgCBF_thr10_MNI.nii.gz -t $TRANSFORM_DIR/PNC-MNI_0warp.nii.gz -t $TRANSFORM_DIR/PNC-MNI_1Affine.mat \
    -r $PWD/data/templates/MNI-2x2x2.nii.gz -d 3 -e 3 -n LanczosWindowedSinc
echo "Transform complete 
"

## 3. Project
export CBF_SURF=$PWD/tmp/z_lh.avgCBF_thr10.mgz
mri_vol2surf --mov $CBF_MNI --reg $FREESURFER_HOME/average/mni152.register.dat --hemi lh \
    --projfrac-avg 0 1 0.1 --surf white --surf-fwhm 3 --o $CBF_SURF
echo "Projection complete"

## 4. Visualize
freeview  -f $SUBJECTS_DIR/fsaverage/surf/lh.inflated::overlay=$CBF_SURF:overlay_method=piecewise:overlay_threshold=20,55,90 \
--viewport 3d