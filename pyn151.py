import os
directory ="C:\Users\whynew.in\OneDrive\Documents\GitHub\brad-python"
for filename in os.listdir(directory):
    full_path = os.path.join(directory, filename)
    print(f"File Name: {filename}")
    print(f"Full Path: {full_path}\n")
