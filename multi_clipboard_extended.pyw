#! python3
# multi_clipboard.pyw - Saves and loads pieces of text to the clipboard.
# Usage: 
#	py.exe multi_clipboard.pyw save <keyword> - Saves clipboard to keyword.
#	py.exe multi_clipboard.pyw list keywords - Loads all keywords to clipboard.
#   py.exe multi_clipboard.pyw delete <keyword> - Deletes key-value pair in the multi clipboard shelf file
#	py.exe multi_clipboard.pyw delete all - Deletes all key-value pairs in the multi clipboard shelf file
#	py.exe multi_clipboard.pyw check <keyword> - Check in key exists in the multi clipboard shelf file
#	py.exe multi_clipboard.pyw <keyword> - Loads keyword linked text to clipboard.

import shelve
import pyperclip
import sys

multi_clipboard_shelf = shelve.open('multi_clipboard_shelf_file')


def save_clipboard_to_shelf():
    multi_clipboard_shelf[sys.argv[2]] = pyperclip.paste()
    print('Saved the clipboard to the multi_clipboard_shelf_file. The clipboard is paired with the keyword \'%s\'' % sys.argv[2])


def copy_all_keywords_in_shelf_file_to_clipboard():
    pyperclip.copy(str(list(multi_clipboard_shelf.keys())))
    print('Copied all keywords to the clipboard')


def copy_all_text_linked_with_keyword_to_clipboard():
    pyperclip.copy(multi_clipboard_shelf[sys.argv[1]])
    print('Copied all text linked with keyword %s to clipboard' % sys.argv[1])


def delete_key_value_pair_in_shelf_file():
    print('Deleting keyword %s and its associated text' % sys.argv[2]
	del multi_clipboard_shelf[sys.argv[2]]
	check_if_keyword_exists_in_shelf_file()


def delete_all_key_value_pairs():
	for keys in multi_clipboard_shelf.keys():
		del  multi_clipboard_shelf[key]
	

def check_if_keyword_exists_in_shelf_file():
    does_key_exist = sys.argv[2] in multi_clipboard_shelf
    print('It is now {} that {} exists in multi_clipboard_shelf'.format(does_key_exist, sys.argv[2])


def run_multi_clipboard():
    if len(sys.argv) == 3:
        if sys.argv[1].lower() == 'save':
            save_clipboard_to_shelf()
        elif sys.argv[1].lower() == 'copy':
            copy_all_keywords_in_shelf_file_to_clipboard()
        elif (sys.argv[1].lower() == 'delete') and (sys.argv[2] in multi_clipboard_shelf):
            delete_key_value_pair_in_shelf_file():
        elif (sys.argv[1].lower() == 'delete') and (sys.argv[2] == 'all'):
            delete_all_key_value_pairs()
        elif sys.argv[1].lower() == 'check':
            check_if_keyword_exists_in_shelf_file()		
    elif (len(sys.argv) == 2) and (sys.argv[1] in multi_clipboard_shelf):
     		copy_all_text_linked_with_keyword_to_clipboard()
    mcbShelf.close()
    
    
run_multi_clipboard()


   
