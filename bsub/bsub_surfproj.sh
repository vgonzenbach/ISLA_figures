#!/bin/bash
cd $(dirname $0)/..

# Compute average image for BASIL
bsub -J avgBASIL Rscript src/compute_avg_BASIL.R

# Register average images
bsub -J regs -w avgBASIL -ti bash src/reg_averages.sh

# Run below in a local computer
:"
# 1. clone repository locally if you haven't already
git clone https://github.com/vgonzenbach/ISLA_paper.git .

# 2. run Jupyter notebook
bash src/run_pysurfer_docker.sh

# 3. Run all cells of notebook/surfplot.ipynb 
# 4. Run `python3 src/join_surf_plots.py`. Make sure to have PIL installed

"
# TODO: Dockerize PIL and other R packages