import os
import sys

dir_path = input('Enter directory path')

if os.path.exists(dir_path):
    all_files = os.listdir(dir_path)
else:
    print(f"{dir_path} is not valid")
    sys.exit(1)


for file in all_files:
    if os.path.isfile(os.path.join(dir_path,file)):
        print(f"{file} is file")
    else:
        print(f"{file} is directory")
