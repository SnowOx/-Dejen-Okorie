#! python3
# brute_force_pdf_password_breaker.py

import PyPDF2
TARGET_PATH = #
WORDS_PATH = #
# Note: PyPDF2 only works with PDF documents that have been encoded with Acrobat 5.0 or earlier

def get_pdf_reader_for(TARGET_FILE):
    pdf_reader = PyPDF2.PdfFileReader(open(TARGET_PATH, "rb"))
    return pdf_reader

def get_english_words_array():
    with open(WORDS_PATH,'r') as in_file:
        read_lines = in_file.readlines()
        english_words = []
        for word in read_lines:
            cleaned_word = word.replace('\n', '')
            english_words.append(cleaned_word)
        return english_words

def decrypt_using(english_words, pdf_reader):
    for word in english_words:
        if pdf_reader.decrypt(word.upper()) == 1:
            print('The password is %s' % word.upper())
            return
        if pdf_reader.decrypt(word.lower()) == 1:
            print('The password is %s' % word.lower())
            return
        print('Not %s or %s' % (word.lower(), word.upper()))

english_words = get_english_words_array()
pdf_reader = get_pdf_reader_for(TARGET_PATH)
decrypt_using(english_words, pdf_reader)

# Solved
