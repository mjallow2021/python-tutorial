#this script will print the directory and list the files present in them.
# uses the os module and os.path.join to join the folder to the current directory
# it also llsts the files in the directory using a for loop.

import os

root = os.path.join('..', 'food')
for directory, subdir_list, file_list in os.walk(root):
    print('Directory:', directory)
    for name in subdir_list:
        print('Subdirectory:', name)
    for name in file_list:
        print('File:', name)
    print()
