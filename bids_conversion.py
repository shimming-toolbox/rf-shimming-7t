import os
import shutil

path_in = '/Users/julien/code/rf-shimming-7t/RF_shimming_project_cleanupload/SubA'
path_out = '/Users/julien/Desktop/rf_shimming_spinalcord_test/sub-01'

# Create dictionary for shim type output
shimtype_dict = {'noRFshim': 'CP',
                 'Noshim': 'CP',
                 'CVred': 'CoV',
                 'PatSpec': 'patient',
                 'PhaseOnly': 'phase',
                 'SAReff': 'SAReff',
                 'Target': 'target',
                 'VolSpec': 'volume'}

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
        file = [os.path.join(path_in, 'MPRAGE', f) for f in os.listdir(os.path.join(path_in, 'MPRAGE')) if shimtype in f and f.endswith(ext)][0]
        shutil.copy2(file, os.path.join(path_out, f'anat/{subject}_acq-{shimtype_dict[shimtype]}_T1w.{ext}'))

# Convert files in GRE_B1 subfolder
# Get the absolute file name of the NIfTI and JSON files under each subfolder of the GRE_B1 subfolder that has the string corresponding to the name of the subfolder in it.
for shimtype in ['CVred', 'Noshim', 'PatSpec', 'PhaseOnly', 'SAReff', 'Target', 'VolSpec']:
    for ext in ['nii.gz', 'json']:
        # Convert GRE data
        # Select the files with the string "gre2d" in it. Select the first pair in the list, which are not corrected for gradient distortion.
        file = [os.path.join(path_in, 'GRE_B1', shimtype, f) for f in os.listdir(os.path.join(path_in, 'GRE_B1', shimtype)) if 'gre2d' in f and f.endswith(ext)][0]
        shutil.copy2(file, os.path.join(path_out, f'anat/{subject}_acq-{shimtype_dict[shimtype]}_T2starw.{ext}'))
        # Convert RF map data
        # Select the files with the string "tfl_b1map" in it. Select the first pair in the list, which is not corrected for gradient distortion, and which corresponds to the magnitude image. Select also the 3rd pair, which corresponds to the RF map.
        file = [os.path.join(path_in, 'GRE_B1', shimtype, f) for f in os.listdir(os.path.join(path_in, 'GRE_B1', shimtype)) if 'tfl_b1map' in f and f.endswith(ext)][0]
        shutil.copy2(file, os.path.join(path_out, f'fmap/{subject}_acq-{shimtype_dict[shimtype]}_part-magnitude_TB1map.{ext}'))
        file = [os.path.join(path_in, 'GRE_B1', shimtype, f) for f in os.listdir(os.path.join(path_in, 'GRE_B1', shimtype)) if 'tfl_b1map' in f and f.endswith(ext)][2]
        shutil.copy2(file, os.path.join(path_out, f'fmap/{subject}_acq-{shimtype_dict[shimtype]}_TB1map.{ext}'))


