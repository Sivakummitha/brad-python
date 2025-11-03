import os
current_directory = os.getcwd()
print(f"Current working directory: {current_directory}")
print(f"Contents of current directory: {os.listdir(current_directory)}")
new_dir_name = "my_new_directory"
os.mkdir(new_dir_name)
print(f"Directory '{new_dir_name}' created.")
os.rmdir(new_dir_name)
print(f"Directory '{new_dir_name}' removed.")
home_directory = os.environ.get("HOME") 
print(f"Home directory (from environment): {home_directory}")