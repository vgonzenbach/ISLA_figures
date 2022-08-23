#!/bin/bash
# Produce pprop barplots

module load pandoc/2.18
cd $(dirname $0)/..

# Produce dataframe of proportion p-values per roi
# TODO: Use Docker/Singularity image for run
bsub -J get_pprop ~/.conda/envs/isla/bin/python3.7 src/get_pprop_by_ROI.py

# Render plots
bsub -w get_pprop -ti Rscript -e "rmarkdown::render('notebook/roi_p.Rmd')"
