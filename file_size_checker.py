#! python3
# file_size_searcher

import os
starting_position = "C:\\"

def show_big_file_details(file):
    file_path, file_size = get_file_details(file)
    print('%s = %s MB' % (file_path, file_size/1000000))

def get_file_details(file):
    file_path = os.path.join(starting_position, file)
    print(file_path)
    file_size = os.path.getsize(file_path)
    print(file_size)
    if file_size > 10000000:
        return(file_path, file_size)

for root, dirs, files in os.walk(starting_position):
    for file in root:
        show_big_file_details(file)
    for file in dirs:
        show_big_file_details(file)
    for file in files:
        show_big_file_details(file)
