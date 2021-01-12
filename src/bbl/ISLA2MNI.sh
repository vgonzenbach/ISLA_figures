export ISLA_IMG=/Users/vgonzenb/PennSIVE/ISLA/data/avg_images/avgISLA/avgISLA_cbf_size2_thr10.nii.gz

antsApplyTransforms -d 3 -e 3 -i $ISLA_IMG -o isla2mni.nii.gz \
-r troubleshoot/MNI-2x2x2.nii.gz \
-t troubleshoot/PNC-MNI_0warp.nii.gz -t troubleshoot/PNC-MNI_1Affine.mat  \
-n LanczosWindowedSinc -v
