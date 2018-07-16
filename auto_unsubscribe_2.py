#! python3
#auto_unsubscribe_2.py

import imapclient
import pyzmail
import pprint
import re
from bs4 import BeautifulSoup
from selenium import webdriver


# I am enjoying using the interspersed definition-operation style below. I have found that the id-o style to improve my
# understanding and testing of the Py that I write.

#EMAIL_ADDRESS = input('email >> ')
EMAIL_ADDRESS = '#'
#PASSWORD = input('password >> ')
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
#pprint.pprint(all_message_html)


def get_unsubscribe_links(html_list):
    unsubscribe_links = []
    for element in html_list:
        #print('element = %s' % element)
        soup = BeautifulSoup(element, 'lxml')
        for result in soup.find_all(href=True, string=re.compile('unsubscribe')): # Getting closer. Purify result.
                unsubscribe_links.append(result)
        print('href links = %s' % unsubscribe_links)
        print('Done')
    print(unsubscribe_links)
    return unsubscribe_links


unsubscribe_links = get_unsubscribe_links(all_message_html)


def open_unsubscribe_link(url):
    driver = webdriver.Firefox()
    driver.get(url)


def open_unsubscribe_links_if_wanted():
    for link in unsubscribe_links:
        answer = input('The link is for %s.\nEnter \'n\' not to open the unsubscribe link' % link)
        if answer != 'n':
            open_unsubscribe_link(link)


#open_unsubscribe_links_if_wanted()
print('Done')
