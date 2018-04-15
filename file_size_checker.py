#! python3
# file_size_searcher

import os

starting_position = os.path.abspath(r'C:\Users\A\Desktop')

def show_big_file_details(file_name):
    get_file_details(file_name)
    try:
        print('%s -- %s MB') % (file_path, file_size)
    except:
        pass
    
def  get_file_details(file_name):
    file_path = os.path.abspath(file_name)
    print(file_path)
    file_size = os.path.getsize(file_path)
    print(file_size)
    if file_size > 100000000:
        return(file_path, file_size)

for root, dirs, files in os.walk(starting_position):
    for file_name in dirs:
        show_big_file_details(file_name)
    for file_name in files:
        show_big_file_details(file_name)

        
