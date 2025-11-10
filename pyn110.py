import zipfile
import os
zip_file = "my_folder_backup.zip"
extract_to = "extracted_folder"
if os.path.exists(zip_file):
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    print("Archive extracted successfully into:", extract_to)
else:
    print("Zip file not found in directory:", os.getcwd())
