#! python3
# file_size_searcher

import os
starting_position = "c:\\Users\\A\\Google Drive\\521Y Graphics"

for dirpath, dirnames, filenames in os.walk(starting_position):
    for filename in filenames:
        file_path = os.path.join(dirpath, filename)
        file_size = os.path.getsize(file_path)
        if file_size > 1000000: 
            print('%s = %s MB' % (file_path, file_size/1000000))
