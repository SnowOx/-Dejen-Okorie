#! python 3

import os
import PyPDF2
from send2trash import send2trash

PASSWORD = 'auburnrain'
START_POSITION = 'C:\\Users\\A\\Google Drive\\OP2\\FolderWithPDF'

def return_if_file_is_pdf(filename):
    if filename.endswith('.pdf'):
        file_path = os.path.join(START_POSITION, filename)
        print(file_path)
        return (filename, file_path)
    else:
        pass

def copy_pages_to_new_PDF_writer_object(file_path, START_POSITION, PASSWORD,
                                        filename):
    pdf_opener = open(file_path, 'rb')
    pdf_reader = PyPDF2.PdfFileReader(pdf_opener)
    pdf_writer = PyPDF2.PdfFileWriter()
    for page_number in range(pdf_reader.numPages):
        page_object = pdf_reader.getPage(page_number)
        pdf_writer.addPage(page_object)
    pdf_opener.close()
    return pdf_writer

def encrypt_pdf(pdf_writer, PASSWORD, filename, START_POSITION):
    pdf_writer.encrypt(PASSWORD)
    filename = filename[:-4]
    encrypted_filename = '%s_encrypted.pdf' % filename
    pdf_opener_for_encrypted_output = open(encrypted_filename, 'wb')
    pdf_writer.write(pdf_opener_for_encrypted_output)
    pdf_opener_for_encrypted_output.close()

    encrypted_file_path = os.path.join(START_POSITION, encrypted_filename)
    return encrypted_file_path

def check_encrypted_file(encrypted_file_path, PASSWORD):
    pdf_read = PyPDF2.PdfFileReader(open(encrypted_file_path, 'rb'))
    encryption_test = pdf_read.decrypt(PASSWORD)
    return encryption_test

def delete_previous_file_if_encryption_successful(file_path, encryption_test,
                                                  encrypted_file_path):
    if encryption_test == 1:
        print('Encryption test successful for: \n%s. \nSending previous file to bin'
              % encrypted_file_path)
        # send2trash.send2trash(file_path)
    else:
        print('Encryption test unsuccessful for %s' % encrypted_file_path)

def iterate_through_files(START_POSITION, PASSWORD):
    os.chdir(START_POSITION)
    for dirpath, dirnames, filenames in os.walk(START_POSITION):
        for element in filenames:
            print('element = ' + element)
            filename, file_path = return_if_file_is_pdf(element)
            print(filename, file_path)
            pdf_writer = copy_pages_to_new_PDF_writer_object(file_path, START_POSITION, PASSWORD, filename)
            encrypted_file_path = encrypt_pdf(pdf_writer, PASSWORD, filename, START_POSITION)
                                                
            encryption_test = check_encrypted_file(encrypted_file_path, PASSWORD)
            print(encryption_test)
            delete_previous_file_if_encryption_successful(file_path, encryption_test, encrypted_file_path)
            print('--------')
    print('complete')

iterate_through_files(START_POSITION, PASSWORD)
