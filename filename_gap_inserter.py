#! python3
# filename_gap_inserter - program to correct gaps in file numbering

import re
import os
import shutil

DIRECTORY = 'C:\\Users\\A\Google Drive\\OP2\\TestFolder'

def put_files_in_sorted_list(folder):
    sorted_filename_list = sorted(os.listdir(folder))
    return sorted_filename_list

def get_list_of_ints(sorted_file_list):
    sorted_file_str = ''.join(sorted_file_list)
    filename_digits_str = re.findall(r'\d+', sorted_file_str)
    filename_int_list = [int(elem) for elem in filename_digits_str]
    return filename_int_list

def define_new_filename_sequence_gaps():
    new_gap_position = int(input('State filename\'s position after which to insert gap/s. \
                            E.g., 1, 2, 3. Note that the first filename position is 1.>> '))
    number_of_new_gaps = int(input('State number of gaps after the filename\'s position >> '))
    return(new_gap_position, number_of_new_gaps)
    
def insert_gaps_into_filename_sequence(filename_int_list, new_gap_position, number_of_new_gaps):
    corrected_values_after_enumerate = []
    for counter, value in enumerate(filename_int_list, 1):
        if counter >= new_gap_position + 1:
            value += number_of_new_gaps
            corrected_values_after_enumerate.append(value)
        else:
            corrected_values_after_enumerate.append(value)                       
    return corrected_values_after_enumerate
        
def get_new_file_names(sorted_file_list, corrected_values_after_enumerate):
    updated_filename_list = []
    for filename, element in zip(sorted_file_list, corrected_values_after_enumerate):
        updated_filename_list_entry = re.sub(r'(\d+)', str(element), filename)
        updated_filename_list.append(updated_filename_list_entry)
    return updated_filename_list

def overwrite_filenames(sorted_filename_list, updated_filename_list, DIRECTORY):
    for sorted_filename, updated_filename in zip(sorted_filename_list, updated_filename_list):
        sorted_filename_path = os.path.join(DIRECTORY, sorted_filename)
        updated_filename_path = os.path.join(DIRECTORY, updated_filename)
        shutil.move(sorted_filename_path, updated_filename_path)

def add_filename_gaps():                                      
    sorted_filename_list = put_files_in_sorted_list(DIRECTORY)
    print('Initial filenames: ' + str(sorted_filename_list))
    filename_int_list = get_list_of_ints(sorted_filename_list)
    new_gap_position, number_of_new_gaps = define_new_filename_sequence_gaps()
    updated_file_sequence = insert_gaps_into_filename_sequence(filename_int_list,
                                                                          new_gap_position,
                                                                          number_of_new_gaps)
    updated_filename_list = get_new_file_names(sorted_filename_list, updated_file_sequence)
    print('Proposed filenames >> ' + str(updated_filename_list))
    overwrite_command = input('Press Y to overwrite filenames with the above proposed filenames >> ')
    if overwrite_command.lower() == 'y':
        overwrite_filenames(sorted_filename_list, updated_filename_list, DIRECTORY)

add_filename_gaps()

# Solved
