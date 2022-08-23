module load pandoc/2.18
cd $(dirname $0)/..
mkdir -p results/tables
# run python script in conda environment
# TODO: change run statement to singularity run after creating Dockerfile

# preprocess data
bsub -J preproc_cbf ~/.conda/envs/isla/bin/python3.7 src/avg_cbf_by_gmd.py

# make plots
bsub -w preproc_cbf -ti Rscript -e "rmarkdown::render('notebook/boxplot_cbf_types.Rmd')"