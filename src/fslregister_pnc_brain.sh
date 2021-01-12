export FREESURFER_HOME=/Applications/freesurfer/7.1.1
source $FREESURFER_HOME/SetUpFreeSurfer.sh

export PNC_BRAIN=data/pncTemplate/pnc_template_brain.nii.gz

fslregister --s fsaverage --mov $PNC_BRAIN --reg brain.dat
#tkregister2 --targ $PNC_BRAIN --mov $PNC_BRAIN --s identity -reg tmp.dat