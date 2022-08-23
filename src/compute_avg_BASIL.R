# Create average for BASIL images
library(neurobase)
library(parallel)

# TODO: parallelize appropriately
niis = system ('find /project/pnc/basilPNC_scanid/*', intern = TRUE)
avg_BASIL = function(thr){
    #' Average images according to threshold
    mask = neurobase::readnii(sprintf('/project/kristin_imco/masks/final_gm%s_cbf.nii.gz', thr))
    image_list = c()

    for (nii in niis){
        image = neurobase::readnii(nii) * mask
        message('loaded image')
        image_list = c(image_list, list(image))
    }
    avg = Reduce('+', image_list) / length(image_list)
    neurobase::writenii(avg, here::here(sprintf('data/mri/avgBASIL_cbf_thr%s.nii.gz', thr)))
}


mclapply(c(10,20), avg_BASIL, mc.cores=2)