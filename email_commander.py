#! python3
# email_commander.py

# When writing, remember that the reader does not care how the program is operating; the reader only cares what the program is doing.

import imapclient
import pyzmail
from bs4 import BeautifulSoup
import subprocess
import logging
logging.basicConfig(filename='emailer_commander_log.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

EMAIL_ADDRESS = '#'
PASSWORD = '#'
SECRET_COMMAND = #
PROGRAM_PATH = #
imap_object = imapclient.IMAPClient('imap.gmail.com', ssl=True) # Change imap_object name to IMAP_OBJECT

 
def get_unique_email_identifiers():
    imap_object.select_folder('Inbox', readonly=True)
    identifier_codes = imap_object.search('ALL')
    return identifier_codes
   

def get_pyzmail_message():
    raw_message = imap_object.fetch([code], ['BODY[]', 'FLAGS'])
    message = pyzmail.PyzMessage.factory(raw_message[code][b'BODY[]'])
    return message
    
    
 def check_if_command_in_message_subject():
    subject = message.get_subject()
    if command in subject:
        return True
    else:
        return False
    
    
def check_messages_for_download_url(identifier_codes):
    for code in identifier_codes:
        print('Searching %s' % code)
        message = get_pyzmail_message()
        if check_if_command_in_message_subject() is True:
            download_url = message.get_payload().decode(message.text_part.charset)
            print('Download command present')
            return download_url


def print_no_command_found():
    print('No download commands present') # Log this
    

def open_program_to_download_from_(url):
    download_program = subprocess.Popen([PROGRAM_PATH, url])
    download_program.wait()
    
    
#Todo: Add logging
    
    
def logout():
    imap_object.logout()
    
    
def engine():
    IMAP_OBJECT.login(EMAIL_ADDRESS, PASSWORD)
    identifier_codes = get_unique_email_identifiers()
    message = get_pyzmail_message()
    download_url = check_messages_for_download_url(identifier_codes)
    logout()
    if download_url != None:
        # Todo: send email notifying of download_program start
        open_program_to_download_from_(url)
        # Todo: send email notifying of download_program termination. Try accessing my emailer package
    else:
        print_no_command_found()
 
