#! python3
# search_for_string_in_text_files.py - Write a program that opens all .txt files in a folder and searches for any # line that matches a user-supplied regular expression. The results should be printed to the screen.

import os
import re
import pprint

raw_string = input('Please enter the string to find in the text files >> ')
search_string = r'\b%s\b' % raw_string
STARTING_POSITION = input('Please enter the directory path to search >> ')

def search_and_return_txt_file_paths(STARTING_POSITION):
    txt_file_paths = []
    for filename in os.listdir(STARTING_POSITION):
        if filename.endswith('.txt'):
            filepath = os.path.join(STARTING_POSITION, filename)
            txt_file_paths.append(filepath)
    return txt_file_paths
        
def search_txt_files_and_print_postive_match_results(txt_file_paths, search_string, raw_string):
    positive_results = []
    for txt_file_path in txt_file_paths:
        with open(txt_file_path, 'r', encoding="utf8") as open_file:
            read_file = open_file.read()
        match_result = re.findall(search_string, read_file)
        if match_result:
            match_instances = 'Found \'%s\' %s times' % (raw_string, len(match_result))
            positive_results.append((txt_file_path, match_instances))
    pprint.pprint(positive_results)

txt_file_paths = search_and_return_txt_file_paths(STARTING_POSITION)
search_txt_files_and_print_postive_match_results(txt_file_paths, search_string, raw_string)

# Solved. Learnt about using /b to indicate regex word boundaries
