#! python3
# text_to_xl

import os
import openpyxl
import random

FILE_FOLDER = 'C:\\Users\\A\\Google Drive\\OP2\\XLTestDocuments'
workbook = openpyxl.Workbook()
sheet = workbook['Sheet']
    
def get_text_filenames_list(directory):
    text_filenames_list = [
        text_filename for text_filename in os.listdir(directory) 
        if text_filename.endswith('.txt')]
    return text_filenames_list

def get_text_content_list(text_filenames_list, directory):
    os.chdir(directory)
    text_contents_list = []
    for filename in text_filenames_list:
        read_content = open(filename).readlines()
        text_contents_list.append(read_content)
    return text_contents_list

def insert_text_and_save_xl_sheet(text_contents_list):
    print('text_contents_list length %s' % len(text_contents_list))
    for i in range(len(text_contents_list)):
        for n in range(len(text_contents_list[i])):
            print(len(text_contents_list[i]))
            cell_content = text_contents_list[i][n]
            cell_location = sheet.cell(column=i+1, row=n+1)
            cell_location.value = cell_content
        
def save_workbook():
    workbook.save('testBook' + str(random.randint(0,1000)) + '.xlsx')

text_filenames_list = get_text_filenames_list(FILE_FOLDER)
text_contents_list = get_text_content_list(text_filenames_list, FILE_FOLDER)
insert_text_and_save_xl_sheet(text_contents_list)
save_workbook()
 
