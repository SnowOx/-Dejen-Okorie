#! python3
# regexSearch.py

import os
import re

DEBUG = True

# Search folder
folder_path = 'C:\Test'
folder_name = os.path.abspath(folder_path)
regex_input = input('Enter regex')
user_regex = re.compile(regex_input)
results_dict = {} # to capture file_name and results
for file_name in folder_name: 
    if file_name.endswith('.txt'):
        results = user_regex.findall(r'%s') % regex_input
        results_dict[file_name] = results
    else:
        pass

while DEBUG == True:
    print(results_dict)
