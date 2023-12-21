import os
import shutil

path_in = '/Users/julien/code/rf-shimming-7t/RF_shimming_project_cleanupload/SubA'
path_out = '/Users/julien/Desktop/rf_shimming_spinalcord/sub-02'

# Get subject name from path_out
subject = os.path.basename(path_out)

# Convert MPRAGE data
# Get the absolute file name of the MPRAGE file that has the string "noRFshim" in it
mprage_file = [os.path.join(path_in, f) for f in os.listdir(path_in) if 'noRFshim' in f][0]
# Copy the file to the output directory with the correct file name: sub-01_acq-CP_T1w.nii.gz
shutil.copy2(mprage_file, os.path.join(path_out, f'{subject}_acq-CP_T1w.nii.gz'))





def process_tfl_b1map(files):
    sorted_files = sorted([f for f in files if 'tfl_b1map' in f])
    processed_files = []
    if len(sorted_files) >= 3:
        # Append _part-mag before the file extension for the first file
        name, ext = os.path.splitext(sorted_files[0])
        processed_files.append(name + '_part-mag' + ext)
        # Include the third file as is
        processed_files.append(sorted_files[2])
    return processed_files

def process_gre2d(files):
    sorted_files = sorted([f for f in files if 'gre2d' in f])
    return sorted_files[:-1] if len(sorted_files) > 1 else sorted_files

def create_bids_structure(base_dir, bids_dir):
    for root, dirs, files in os.walk(base_dir):
        # Filter out system files like .DS_Store
        files = [f for f in files if not f.startswith('.')]

        tfl_b1map_files = process_tfl_b1map(files)
        gre2d_files = process_gre2d(files)

        processed_files = tfl_b1map_files + gre2d_files + [f for f in files if 'tfl_b1map' not in f and 'gre2d' not in f]

        for file in processed_files:
            subject_id = '01'  # Modify this as per your dataset
            category = 'fmap' if 'b1map' in file else 'anat'

            new_file_name = f'sub-{subject_id}_{file}'
            new_file_path = os.path.join(bids_dir, category, new_file_name)

            os.makedirs(os.path.dirname(new_file_path), exist_ok=True)

            original_file_path = os.path.join(root, file)
            if os.path.exists(original_file_path):
                shutil.copy2(original_file_path, new_file_path)
                print(f'File {file} moved to {new_file_path}')
            else:
                print(f'Warning: File {original_file_path} not found. Skipping.')

if __name__ == "__main__":
    original_dir = '/Users/julien/code/rf-shimming-7t/RF_shimming_project_cleanupload/SubA'
    bids_dir = '/Users/julien/Desktop/rf_shimming_spinalcord/sub-01bis'
    create_bids_structure(original_dir, bids_dir)
