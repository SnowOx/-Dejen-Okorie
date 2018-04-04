#! python3
# textFileSearch.py - Write a program that opens all .txt files in a folder and searches for any # line that matches a user-supplied regular expression. The results should be printed to the screen.

import os
import re

string = input('Please enter the string to find in the text files >> ')
files = []

for filename in os.listdir('.'):
    if filename.endswith('.txt'):
        print('Now searching >>>', filename)
        for line in filename:
            if bool(re.search(string, string)) == True:
                print(filename, 'line: ', line)
                files.append(line) #Update dictionary
            else:
                pass
        print(f'Completed search of {filename} >>>')
        
    else:
        print('No matches for {} found in {}'.format(string, filename))

print('Search complete')
print('The string appeared in ', files)


		
