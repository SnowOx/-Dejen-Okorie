
#! python3
# walk_copy_files.py

import os
import shutil
import logging

# STARTING_POSITION = input('Enter path from where to begin walk')
# OUTPUT_POSITION= input('Enter directory to copy files to')
STARTING_POSITION = os.path.abspath(r'C:\Users\A\Downloads')
OUTPUT_POSITION = os.path.abspath(r'C:\Users\A\Desktop\OutputFolder')
 
def file_copier(file_name, file_source, file_destination):
    if file_name.endswith('.pdf') or file_name.endswith('.jpg'):
        shutil.copy(file_source, file_destination)
        print('Copied %s to %s' % file_name, file_destination)
    else:
        pass

def file_locations(file_name):
    file_name_path = os.path.abspath(file_name)
    file_name_destination = os.path.join(OUTPUT_POSITION, file_name)
    print(file_name_path, file_name_destination)
    return (file_name_path, file_name_destination)

for root, dirs, files in os.walk(STARTING_POSITION):
    print(STARTING_POSITION)
    for file_name in root:
        print(file_name)
        file_locations(file_name)
        print(file_name_path + 'return sucessful')
        file_copier(file_name, file_name_path, file_name_destination)
    for file_name in dirs:
        file_locations(file_name)
        file_copier(file_name, file_name_path, file_name_destination)
    for file_name in files:
        file_locations(file_name)
        file_copier(file_name, file_name_path, file_name_destination)
        
print('Walk complete')
        
