import os
import sys
# Using os.walk(dir) to check its functionality
dir_path = input("Enter file directory path")

# checked if directory path is valid or not
if os.path.exists(dir_path):
    dir_content = os.listdir(dir_path)
else:
    os.exit(1)
print(list(os.walk(dir_path)))


# CONCLUSION: os. walk visits all the files- directory present in the given path and come up to tuples