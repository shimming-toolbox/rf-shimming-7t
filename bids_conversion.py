import os
import shutil

path_in = '/Users/julien/code/rf-shimming-7t/RF_shimming_project_cleanupload/SubA'
path_out = '/Users/julien/Desktop/rf_shimming_spinalcord/sub-02'

# Create dictionary for shim type output
shimtype_dict = {'noRFshim': 'CP', 'CVred': 'CVred'}

# Get subject name from path_out
subject = os.path.basename(path_out)

# Create output directory
os.makedirs(path_out, exist_ok=True)
os.makedirs(os.path.join(path_out, 'anat'), exist_ok=True)
os.makedirs(os.path.join(path_out, 'fmap'), exist_ok=True)

# Convert MPRAGE data
# Get the absolute file name of the NIfTI and JSON files under the MPRAGE subfolder, that has the string "noRFshim" in it
for shimtype in ['noRFshim', 'CVred']:
    for ext in ['nii.gz', 'json']:
        mprage_file = [os.path.join(path_in, 'MPRAGE', f) for f in os.listdir(os.path.join(path_in, 'MPRAGE')) if shimtype in f and f.endswith(ext)][0]
        shutil.copy2(mprage_file, os.path.join(path_out, f'anat/sub-{subject}_acq-{shimtype_dict[shimtype]}_T1w.{ext}'))

# Convert RF map data


        