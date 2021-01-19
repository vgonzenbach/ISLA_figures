import os
import subprocess
from surfer import Brain, project_volume_data
from mayavi import mlab

mlab.init_notebook(backend='png')

# Set environment variables
# os.environ['FREESURFER_HOME'] = '/Applications/freesurfer/7.1.1'
# os.environ['SUBJECTS_DIR'] = os.path.join(os.environ['FREESURFER_HOME'], 'subjects')
subprocess.run(os.path.join(os.environ['FREESURFER_HOME'], 'SetUpFreeSurfer.sh'))

brain = Brain("fsaverage5", "split", "inflated",
              views=['lat', 'med'], background="white")

mri_file = os.path.join(os.getcwd(), 'data/mri/reg/avgCBF_thr10_MNI.nii.gz')
reg_file = os.path.join(os.environ["FREESURFER_HOME"], "average/mni152.register.dat")
surf_data_lh = project_volume_data(mri_file, "lh", reg_file, smooth_fwhm=3)
#surf_data_rh = project_volume_data(mri_file, "rh", reg_file)
brain.add_overlay(surf_data_lh,min=0, max=90, name="cbf_lh", hemi='lh')
brain