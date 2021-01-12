# Surface Projection

Purpose: to showcase 3 possible variations (A, B, C) on surface projection of PNC average CBF image.

## A. `recon-all`, project to `fsaverage`

1. Run `recon-all` on `pnc_template`
2. Project CBF image (in pnc template space) to `fsaverage`, with `--regheader pnc_template`

[See script](a_vol2surf.sh)  
[See resulting figure](./results/figures/surf/a_lh.cbf_surf.png)
[Get intermediate .mgz file](./data/surf/a_lh.avgCBF_thr10.mgz)
## B. No `recon-all`, project to fsaverage

1. Use `fslregister` to compute `register.dat` 
2. Project CBF image to `fsaverage`, with `--reg register.dat`

[See script](b_vol2surf.sh)  
[See resulting figure](./results/figures/surf/b_lh.cbf_surf.png)
[Get intermediate .mgz file](./data/surf/b_lh.avgCBF_thr10.mgz)

## C. `recon-all`, project to `pnc_template`

1. Run `recon-all` on `pnc_template`
2. Use `fslregister` to compute `indetity.dat` 
3. Project CBF image to `fpnc_template`, with `--reg identity.dat`

[See script](c_vol2surf.sh)  
[See resulting figure](./results/figures/surf/c_lh.cbf_surf.png)
[Get intermediate .mgz file](./data/surf/c_lh.avgCBF_thr10.mgz)