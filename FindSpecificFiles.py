import os
import sys
# counting the no. of files present with the given file eextension

dir_path = input("Enter file directory path")

# checked if directory path is valid or not
if os.path.exists(dir_path):
    dir_content = os.listdir(dir_path)
    file_extension = input('Enter file extension as .sh | .py | .cpp etc.')
else:
    sys.exit(1)
file_found = list()
count=0
# checking if file ends with that extension
for file in dir_content:
    if file.endswith(file_extension):
        file_found.append(file)
        count=count+1
if count==0:
    print(f'No file found with {file_extension} file exntension')
print(f"No of file found : {count}")
print("Files are as follows :")
for file in file_found:
    print(file)