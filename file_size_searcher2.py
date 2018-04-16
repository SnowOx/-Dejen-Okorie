#! python3
# file_size_searcher2.py

import os
import pprint
starting_position = r'C:\Users\A\Downloads'

def get_size_and_path(filename):
    print('Accessed %s' % filename)
    file_path = os.path.join(starting_position, filename)
    try:
        file_size = os.path.getsize(file_path)
        if file_size > 1000000:
            print('%s has a filesize of %s MB. Path = %s' % \
                  (filename, (file_size/1000000), file_path))
            big_file_dict[filename] = {}
            big_file_dict[filename][file_path] = file_size
    except:
        print('%s appears not to be a file' % filename)
        
        
big_file_dict = {}
for root, dirs, files in os.walk(starting_position):
    for filename in root:
        get_size_and_path(filename)
    for filename in dirs:
        get_size_and_path(filename)
    for filename in files:
        get_size_and_path(filename)
pprint.pprint(big_file_dict)
