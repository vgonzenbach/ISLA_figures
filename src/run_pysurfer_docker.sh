docker run -it --rm -p 8888:8888 -v $PWD:/work -v $PWD/data/freesurfer/license.txt:/opt/freesurfer-6.0.1/license.txt \
    -v $PWD/data/freesurfer/fsaverage5:/opt/freesurfer-6.0.1/subjects/fsaverage5 \
    kaczmarj/pysurfer-jupyter