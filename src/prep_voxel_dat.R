library(oro.nifti)
library(fslr)
#' load thr10 images -> 
#' process all-, boundary-, inner-voxel images in different dataframes -> 
#' repeat for thr20 images ->
#' create factor with 6 levels: thr-by-voxelgroup -> add relevant factor to each

## Threshold: 10 %
# Original
dat_10_orig = data.frame(gmd = as.vector(readnii("data/mri/avgGMD_CBF_thr10.nii.gz")), 
                         cbf = as.vector(readnii("data/mri/avgCBF_thr10.nii.gz")))
dat_10_orig$type = rep("10% all", nrow(dat_10_orig))

# Inner voxels
dat_10_inner = data.frame(gmd = as.vector(readnii(fsl_erode(file = "data/mri/avgGMD_CBF_thr10.nii.gz"))),
                          cbf = as.vector(readnii(fsl_erode(file = "data/mri/avgCBF_thr10.nii.gz"))))
dat_10_inner$type = rep("10% inner", nrow(dat_10_inner))

# Boundary voxels
dat_10_bound = data.frame(gmd = as.vector(readnii("data/mri/avgGMD_CBF_thr10.nii.gz") - readnii(fsl_erode(file = "data/mri/avgGMD_CBF_thr10.nii.gz"))),
                          cbf = as.vector(readnii("data/mri/avgCBF_thr10.nii.gz") - readnii(fsl_erode(file = "data/mri/avgCBF_thr10.nii.gz"))))
dat_10_bound$type = rep("10% boundary", nrow(dat_10_bound))

## Threshold: 20 %
# Original
dat_20_orig = data.frame(gmd = as.vector(readnii("data/mri/avgGMD_CBF_thr20.nii.gz")), 
                         cbf = as.vector(readnii("data/mri/avgCBF_thr20.nii.gz")))
dat_20_orig$type = rep("20% all", nrow(dat_20_orig))

# Inner voxels
dat_20_inner = data.frame(gmd = as.vector(readnii(fsl_erode(file = "data/mri/avgGMD_CBF_thr20.nii.gz"))),
                          cbf = as.vector(readnii(fsl_erode(file = "data/mri/avgCBF_thr20.nii.gz"))))
dat_20_inner$type = rep("20% inner", nrow(dat_20_inner))

# Boundary voxels   
dat_20_bound = data.frame(gmd = as.vector(readnii("data/mri/avgGMD_CBF_thr20.nii.gz") - readnii(fsl_erode(file = "data/mri/avgGMD_CBF_thr20.nii.gz"))),
                          cbf = as.vector(readnii("data/mri/avgCBF_thr20.nii.gz") - readnii(fsl_erode(file = "data/mri/avgCBF_thr20.nii.gz"))))
dat_20_bound$type = rep("20% boundary", nrow(dat_20_bound))

## Merge all dataframes
dat = rbind(dat_10_orig, dat_10_inner, dat_10_bound, dat_20_orig, dat_20_inner, dat_20_bound)
dat$type = as.factor(dat$type)

saveRDS(dat, 'data/voxel_data.rds')
