#! python3
# regexSearch.py

import os
import re

# Search folder
folder_path = input('Enter folder path to search for regex ')
folder_contents = os.listdir(folder_path)
user_regex = input(r'Enter regex ')

results_dict = {}
def store_and_show_results():
    print('File %s is a .txt file. The program found \'%s\' %s times' %
          (file_name, user_regex, len(results)))
    print(results)
    results_dict[file_name] = results
    
for file_name in folder_contents:
    if file_name.endswith('.txt'):
        with open(os.path.join(folder_path, file_name), 'r') as input_file:
            text_to_search = input_file.read()
        results = re.findall(user_regex, text_to_search)
        store_and_show_results()   
    else:
        print('File %s is not a .txt file' % file_name)

# Solved

