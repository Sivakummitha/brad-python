import os
file_path = "zomato.csv"
if os.path.exists(file_path):
    print("File exists.")
    size = os.path.getsize(file_path)
    print(f"Size of the file: {size} bytes")
else:
    print("File does not exist.")
