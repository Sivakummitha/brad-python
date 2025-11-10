import os
import shutil
import zipfile
folder_path = "my_folder"
output_zip = "my_folder_backup"
if os.path.exists(folder_path) and os.path.isdir(folder_path):
    shutil.make_archive(output_zip, 'zip', folder_path)
    print("Folder successfully converted to ZIP file!")
else:
    print("Folder not found in the current directory:", os.getcwd())
