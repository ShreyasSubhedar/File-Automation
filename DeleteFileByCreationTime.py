# Deleting the file if creation date is exceeding 24 hrs timestamp 
import os
import datetime
import sys

dir_path = input("Enter file directory path")

# checked if directory path is valid or not
if os.path.exists(dir_path):
    dir_content = os.listdir(dir_path)
else:
    sys.exit(1)


for file in dir_content:
    file_full_path = os.path.join(dir_path, file)
    file_creation_time = os.path.getctime(file_full_path)
    dt_object = datetime.datetime.fromtimestamp(file_creation_time)
    if dt_object.date() < datetime.datetime.now().date():
        print(f'{file} going to delete')
    else:
        print(f'{file} going to saved in server for today')
