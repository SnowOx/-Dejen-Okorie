#! python3
# auto_unsubscribe_2.py

import pyzmail
import imapclient
import imaplib
imaplib._MAXLINE = 10000000
import pprint
from bs4 import BeautifulSoup
import webbrowser


EMAIL_ADDRESS = input('email >> ')
PASSWORD = input('password >> ')
IMAP_OBJECT = imapclient.IMAPClient('imap.gmail.com', ssl=True)
IMAP_OBJECT.login(EMAIL_ADDRESS, PASSWORD)


def select_the_email_folder_to_search():
    email_folders = IMAP_OBJECT.list_folders()
    pprint.pprint('Your emails are in the following folders:')
    for folder in email_folders:
        pprint.pprint(folder[2])
    folder_name = str(input('Enter the folder that you want to search '))
    return folder_name


def get_email_unique_codes():
    folder_name = select_the_email_folder_to_search()
    IMAP_OBJECT.select_folder(folder_name, readonly=True)
    uid_codes = IMAP_OBJECT.search(['ALL'])
    return uid_codes


def get_message_from_(identifier):
    raw_message = IMAP_OBJECT.fetch([identifier], ['BODY[]', 'FLAGS'])
    message = pyzmail.PyzMessage.factory(raw_message[identifier][b'BODY[]'])
    return message


def get_html_from_(message, identifier):
    try:
        if message.html_part is not None:
            html_from_single_message = message.html_part.get_payload().decode(message.html_part.charset)
            return html_from_single_message
    except (TypeError, UnicodeDecodeError) as error:
        print(f'{identifier} suffered a TypeError with the message\'{error}\'. Skipping this email')


def get_html(unique_codes):
    input(f'There are {len(unique_codes)} emails to scan. Proceed?')
    all_message_html = []
    for identifier in unique_codes:
        print(f'Scanning email {identifier}')
        message = get_message_from_(identifier)
        if get_html_from_(message, identifier):
            all_message_html.append(get_html_from_(message, identifier))
    return all_message_html


def get_unsubscribe_links(html_list):
    unsubscribe_links = []
    for element in html_list:
        soup = BeautifulSoup(element, 'lxml')
        for tag in soup.find_all(href=True):
                if 'unsubscribe' in tag['href']:  # J Query 1: I originally wrote ##if 'unsubscribe' and 'http' in tag['href']:## Why was this ineffective?
                    unsubscribe_links.append(tag['href'])
    return unsubscribe_links


def open_unsubscribe_link(url):
    webbrowser.open(url)


def open_unsubscribe_links_if_wanted(unsubscribe_links):
    for link in unsubscribe_links:
        answer = input('The link is for %s.\nEnter \'n\' not to open the unsubscribe link ' % link)
        if answer != 'n':
            print('Opening unsubscribe link')
            open_unsubscribe_link(link)


def engine():
    unique_codes = get_email_unique_codes()
    all_message_html = get_html(unique_codes)
    unsubscribe_links = get_unsubscribe_links(all_message_html)
    open_unsubscribe_links_if_wanted(unsubscribe_links)
    print('Filtered all url links containing \'unsubscribe\' ')


engine()
