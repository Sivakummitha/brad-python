import os
import time
import shutil
folder_name = "TestFolder"
if not os.path.exists(folder_name):
    os.mkdir(folder_name)
print(f"Folder '{folder_name}' created.\n")
file_names = ["sivafile1.txt", "sivafile2.txt", "sivafile3.txt"]
for file in file_names:
    with open(os.path.join(folder_name, file), "w") as f:
        f.write(f"This is {file}\n")
print("Files created successfully.\n")
files = os.listdir(folder_name)
print(f"Total files: {len(files)}\n")
for file in files:
    file_path = os.path.join(folder_name, file)
    creation_time = time.ctime(os.path.getctime(file_path))
    modification_time = time.ctime(os.path.getmtime(file_path))
    print(f"File: {file}")
    print(f"  Created On: {creation_time}")
    print(f"  Modified On: {modification_time}\n")
for file in files:
    os.remove(os.path.join(folder_name, file))
print("All files deleted.\n")
shutil.rmtree(folder_name, ignore_errors=True)
print(f"Folder '{folder_name}' deleted successfully.")
