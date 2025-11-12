import os
new_dir = "MyNewFolder"
if not os.path.exists(new_dir):
    os.mkdir(new_dir)
    print(f"Directory '{new_dir}' created successfully!")
else:
    print(f"Directory '{new_dir}' already exists.")
os.chdir(new_dir)
print("Now working in:", os.getcwd())

