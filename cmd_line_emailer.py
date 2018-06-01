#! python3
# cmd_line_emailer.py

import time
import sys
from selenium import webdriver

WEBPAGE = 'https://mail.protonmail.com/login'

def get_browser_object():
    browser_object = webdriver.Firefox()
    return browser_object

def load_webpage(browser_object):
    browser_object.get(WEBPAGE)

def add_time_delay(seconds):
    time.sleep(int(seconds))

def get_login_input():
    username = str(input('Enter username'))
    password_1 = str(input('Enter password 1'))
    password_2 = str(input('Enter password 2'))
    return(username, password_1, password_2)

def enter_login_information(username, password_1,browser_object):
    username_field = browser_object.find_element_by_css_selector('#username')
    username_field.send_keys(username)
    password_1_field = browser_object.find_element_by_css_selector('#password')
    password_1_field.send_keys(password_1)
    html_element = browser_object.find_element_by_tag_name('html')
    html_element.send_keys(Keys.ENTER)
    add_time_delay(5)
    try:
        password_2_field = browser_object.find_element_by_css_selector('#password')
        password_2_field.send_keys(password_2)
        html_element = browser_object.find_element_by_tag_name('html')
        html_element.send_keys(Keys.ENTER)
    except:
        raise ValueError('The password_2 login failed')

def get_recipient_email_address(): # Perhaps add default to test other functtionality
    recipient_email_address = sys.argv[2]
    return recipient_email_address

def get_message_string():
    message_string = sys.argv[2:]
    return message_string

def open_new_message(browser_object):
    compose_button = browser_object.find_element_by_css_selector(
        '#pm_sidebar > button')
    compose_button.click()
    add_time_delay(2)

def write_message(browser_object, recipient_email_address, message_subject, message_string):
    subject_field = browser_object.find_element_by_css_selector(
        '#uid2 > div.meta.composer-meta > div.row.subjectRow.composer-field-Subject.composerSubject-container > input')
    subject_field.send_keys(recipient_email_address)
    to_field = browser_object.find_element_by_css_selector('#autocompleteedq9vt3v7m-1527857257046')
    to_field.send_keys(recipient_email_address)
    message_body = browser_object.find_element_by_css_selector('body > div:nth-child(1)')
    message_body.send_keys(message_string)

def click_send_email(browser_object):
    click_send_email_button = browser_object.find_element_by_css_selector(
        '#uid2 > footer > div > button.pm_button.primary.mobileFull.composer-btn-send.btnSendMessage-btn-action')
    click_send_email_button.click()
    

#Engine
    
#recipient_email_address = get_recipient_email_address(sys.argv) # Perhaps add default to test other functtionality
recipient_email_address = '000td000@gmail.com'
#message_string = get_message_string(sys.argv)
message_string = 'test test test 123 test'
browser_object = get_browser_object()
load_webpage(browser_object)
#username, password_1, password_2 = get_login_input()
username = '1239'
password_1 = '0001'
password_2 = '0001'
enter_login_information(username, password_1,password_2, browser_object)
open_new_message(browser_object)
write_message(browser_object, recipient_email_address, message_subject, message_string)
click_send_email(browser_object)
