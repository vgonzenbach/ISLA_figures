#!/bin/bash
source /Applications/freesurfer/7.1.1/SetUpFreeSurfer.sh
export SUBJECTS_DIR=/Users/vgonzenb/PennSIVE/ISLA/output

# Run recon-all on template
recon-all -i pncTemplate/pnc_template.nii.gz -s pnc_template -all
recon-all -i pncTemplate/pnc_template_brain.nii.gz -s pnc_template_brain -all
