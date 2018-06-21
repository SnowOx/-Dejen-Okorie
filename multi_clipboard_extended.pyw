#! python3
# multi_clipboard.pyw - Saves and loads pieces of text to the clipboard.
# Usage:
#	py.exe multi_clipboard.pyw save <keyword> - Saves clipboard to keyword.
#	py.exe multi_clipboard.pyw load keywords - Loads all keywords to clipboard.
#   py.exe multi_clipboard.pyw delete <keyword> - Deletes key-value pair in the multi clipboard shelf file
#	py.exe multi_clipboard.pyw delete all keywords - Deletes all key-value pairs in the multi clipboard shelf file
#	py.exe multi_clipboard.pyw check <keyword> - Check in key exists in the multi clipboard shelf file
#	py.exe multi_clipboard.pyw <keyword> - Loads keyword linked text to clipboard.
#   py.exe multi_clipboard.pyw show keywords - Loads all keywords to clipboard.

import shelve
import pyperclip
import sys

multi_clipboard_shelf = shelve.open('multi_clipboard_shelf_file')


def save_clipboard_to_shelf():
    multi_clipboard_shelf[sys.argv[2]] = pyperclip.paste()
    print('Saved the clipboard to the multi_clipboard_shelf_file. The clipboard is paired with the keyword \'%s\''
          % sys.argv[2])


def copy_all_keywords_in_shelf_file_to_clipboard():
    pyperclip.copy(str(list(multi_clipboard_shelf.keys())))
    print('Loaded all keywords to the clipboard as a list')


def copy_all_text_linked_with_keyword_to_clipboard():
    if sys.argv[1] in multi_clipboard_shelf:
        pyperclip.copy(multi_clipboard_shelf[sys.argv[1]])
        print('Copied all text linked with keyword %s to clipboard' % sys.argv[1])
    else:
        print('Did not find {} in multi_clipboard_shelf. Did not copy anything to the clipboard.'.format(sys.argv[1]))


def show_all_keywords():
    if multi_clipboard_shelf:
        for key, value in multi_clipboard_shelf.items():
            print('The keyword is:\n{}\nThe associated text is:\n{}\n'.format(key,value))
    else:
        print('There are no keywords or associated text in the multi_clipboard_shelf')


def delete_key_value_pair_if_in_shelf_file():
    if sys.argv[2] in multi_clipboard_shelf:
        print('Deleting keyword %s and its associated text' % sys.argv[2])
        del multi_clipboard_shelf[sys.argv[2]]
        check_if_keyword_exists_in_shelf_file()
    else:
        print('Did not find {} in multi_clipboard_shelf. Did not delete anything.'.format(sys.argv[1]))

        
def delete_all_key_value_pairs():
    for key in multi_clipboard_shelf.keys():
        del multi_clipboard_shelf[key]
    print('Deleted all keywords and associated text')


def check_if_keyword_exists_in_shelf_file():
    does_key_exist = sys.argv[2] in multi_clipboard_shelf
    print('It is now {} that {} exists in multi_clipboard_shelf'.format(does_key_exist, sys.argv[2]))


def print_no_key_value_pair_found_message():
    print('No keyword or associated text was found')


def run_multi_clipboard():
    if len(sys.argv) == 4:
        delete_all_key_value_pairs()
    if len(sys.argv) == 3:
        if sys.argv[1].lower() == 'show':
            show_all_keywords()
        if sys.argv[1].lower() == 'save':
            save_clipboard_to_shelf()
        elif sys.argv[1].lower() == 'load':
            copy_all_keywords_in_shelf_file_to_clipboard()
        elif (sys.argv[1].lower() == 'delete'):
            delete_key_value_pair_if_in_shelf_file()
        elif sys.argv[1].lower() == 'check':
            check_if_keyword_exists_in_shelf_file()
    elif (len(sys.argv) == 2):
        copy_all_text_linked_with_keyword_to_clipboard()
    multi_clipboard_shelf.close()


run_multi_clipboard()

# Solved
