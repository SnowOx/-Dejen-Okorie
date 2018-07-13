#! python3
#auto_unsubscribe_2.py

import imapclient
import pyzmail
import pprint
import re
from bs4 import BeautifulSoup

# I am enjoying using the interspersed definition-operation style below. I have found that the id-o style to improve my 
# understanding and testing of the Py that I write.

EMAIL_ADDRESS = '#'
PASSWORD = '#'

imap_object = imapclient.IMAPClient('imap.gmail.com', ssl=True)
imap_object.login(EMAIL_ADDRESS, PASSWORD)
#imap_object.select_folder('[Gmail]/All Mail', readonly = True)
imap_object.select_folder('Inbox', readonly = True)
UID_codes = imap_object.search('ALL')
print(UID_codes)


def get_message_html(UID_codes):
    all_message_html = []
    for code in UID_codes:
        print('UID = %s' % code)
        raw_message = imap_object.fetch([code], ['BODY[]', 'FLAGS'])
        message = pyzmail.PyzMessage.factory(raw_message[code][b'BODY[]'])
        if message.html_part != None:
            html_from_single_message = message.html_part.get_payload().decode(message.html_part.charset)
            all_message_html.append(html_from_single_message)
    return all_message_html


all_message_html = get_message_html(UID_codes)
pprint.pprint(all_message_html)


def filter_for_unsubscribe_links(href):
    return href and re.compile('unsubscribe').search(href)
    return href and re.compile('remove').search(href)
    return href and re.compile('out').search(href)


def get_unsubscribe_links(html_list):
    unsubscribe_links = []
    for element in html_list:
        soup = BeautifulSoup(element, 'lxml')
        filtered_links = soup.find_all(href=filter_for_unsubscribe_links)
        unsubscribe_links.append(filtered_links)
        print('Done')
    print(unsubscribe_links)


get_unsubscribe_links(all_message_html)
# Working. Get only links


print('Done')
