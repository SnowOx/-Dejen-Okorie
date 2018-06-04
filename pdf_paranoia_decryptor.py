#! python3
# pdf_paranoia_revisited.py

import PyPDF2
import os

PASSWORD = 'rain'
START_POSITION = 'C:\\Users\\A\Desktop\\South US Journey Documents'

decryption_failed = []
for dirpath, dirnames, filenames in os.walk(START_POSITION):
    os.chdir(dirpath)
    for filename in filenames:
        if filename.endswith(".pdf"):
            # Open pdf file
            input_path = os.path.join(dirpath, filename)
            print(input_path)
            # Read pdf file and add its pages to pdf_writer
            pdf_reader = PyPDF2.PdfFileReader(open(input_path, "rb"))
            if pdf_reader.isEncrypted == True:
                pdf_reader.decrypt(PASSWORD)
                pdf_writer = PyPDF2.PdfFileWriter()
                for page_number in range(pdf_reader.numPages):
                    pdf_writer.addPage(pdf_reader.getPage(page_number))
                # Create output file
                decrypted_path = input_path[:-4] + "_decrypted.pdf"
                decrypted_output_file = open(decrypted_path, "wb")
                # Write out pages from pdf_writer to output_pdf_file
                pdf_writer.write(decrypted_output_file)
                decrypted_output_file.close()
                # Check newly encrypted file's decryption
                opened_newly_decrypted_file = open(decrypted_path, "rb")
                checking_pdf_reader = PyPDF2.PdfFileReader(opened_newly_decrypted_file)
                if checking_pdf_reader.isEncrypted == False:
                    print("Successfully decrypted")
                else:
                    print("Unsuccessful decrypted")
                    decryption_failed.append(filename)

if decryption_failed != []:
    print('The following files failed decryption tests: ')
    print(str(decryption_failed))
elif decryption_failed == []:
    print('All encrypted files that os.walk encountered have been decrypted')

# Solved
