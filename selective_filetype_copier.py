#! python3
# selective_filetype_copier.py

import os
import shutil

input_position = os.path.abspath('C:\\Users\\A\\Desktop\\TestFolder')
output_position = os.path.abspath('C:\\Users\\A\\Desktop\\OutputFolder')
 
def get_file_paths(file_name, input_position, output_position):
    file_name_source = os.path.join(input_position, file_name)
    file_name_destination = os.path.join(output_position, file_name)
    return (file_name_source, file_name_destination)

def return_only_desired_file_types(file_name):
    if file_name.endswith('.pdf') or file_name.endswith('.jpg'):
        return file_name

def file_copier(file_name, file_source, file_destination):
    shutil.copy(file_source, file_destination)
    print('\nCopied %s \nfrom %s \nto %s' % (file_name, file_source, file_destination))

for dirpath, dirnames, filenames in os.walk(input_position):
    for file_name in filenames:
        file_name_source, file_name_destination = get_file_paths(file_name, input_position, output_position)
        desired_file_name = return_only_desired_file_types(file_name)
        if desired_file_name:       
            file_copier(desired_file_name, file_name_source, file_name_destination)
        
print('\nDone')

# Solved!
