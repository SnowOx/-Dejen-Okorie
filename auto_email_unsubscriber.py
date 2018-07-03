#! python3
# auto_email_unsubscriber.py
# for gmail accounts (initially)

import imapclient
imaplib._MAXLINE = 10000000
import pyzmail
from bs4 import BeautifulSoup


PASSWORD = #
EMAIL_ADDRESS = # 


imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)

imapObj.login(EMAIL_ADDRESS, PASSWORD)

# Google app pwords https://support.google.com/accounts/answer/185833?hl=en/

all_email_folders = imapObj.list_folders()


def return_every_UID_of_messages_in_email_folder(folder)
	imapObj.select_folder(folder)
message_UIDs = imapObj.search(['ALL'])
	print(message_UIDs)  # to debug
	return message_UIDs


def get_raw_email_message_from_UID_code(UID):
	raw_message = pyzmail.PyzMessage.factory(rawMessages[UID_code]['BODY[]'])
	return raw_message


def get_html_email_body_from_raw_message(message):
	assert message.text_part != None
	assert message.html_part != None
	html_email_body = message.html_part.get_payload().decode(message.html_part.charset)
	

def get_email_soup_from_email_html(html):
	email_soup = BeautifulSoup(html, ‘lxml’)
return email_soup


def return_link_if_email_contains _unsubscribe_or_optout_link():
  link_filters = ["a[href*=unsubscribe]", “a[href*=OptOut]”]
    for element in link_filters:
      if email_soup.find(element) != None:
        return element
      else:
        print(‘No unsubscribe link found in %s’ % UID)
	
# open each of links ## Check working before continuing

# Engine
	
for folder in all_email_folders:
message_UIDs = return_every_UID_of_messages_in_email_folder(folder)
for UID in message_UIDs:
	raw_message  = get_raw_email_message_from_UID_code
	html_email_cody = get_html_email_body_from_raw_message(raw_message)
	email_html = get_email_soup_from_email_html(html)
	element = return_link_if_email_contains _unsubscribe_or_optout_link()
