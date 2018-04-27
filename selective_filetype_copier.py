#! python3
# selective_filetype_copier.py

import os
import shutil

input_position = os.path.abspath('C:\\Users\\A\\Downloads')
output_position = os.path.abspath('C:\\Users\\A\\Desktop\\OutputFolder')
 
def return_only_desired_file_types(file_name):
    if file_name.endswith('.pdf') or file_name.endswith('.jpg'):
        return file_name
    
def file_copier(file_name, file_source, file_destination):
        shutil.copy(file_source, file_destination)
        print('Copied %s from %s >>> %s' % file_name, file_source, file_destination)

def get_file_paths(file_name, input_position, output_position):
    file_name_source = os.path.join(file_name, input_position_
    file_name_destination = os.path.join(file_name, output_position)
    return (file_name_source, file_name_destination)

for dirpath, dirnames, filenames in os.walk(starting_position):
    for filename in filenames:
        get_file_paths(file_name, input_position, output_position) = file_name_source, file_name_destination
        return_only_desired_file_types(file_name) = file_name
        if file_name:              
            file_copier(file_name, file_name_source, file_name_destination)
        
print('Done')
        
