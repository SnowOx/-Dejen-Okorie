#! python3
# cmd_line_emailer.py

import time
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import getpass

WEBPAGE = 'https://mail.protonmail.com/login'

def get_browser_object():
    browser_object = webdriver.Firefox()
    return browser_object

def load_webpage(browser_object):
    browser_object.get(WEBPAGE)

def add_time_delay(seconds):
    time.sleep(int(seconds))

def get_login_input():
    username = '1239'
    #password_1 = input('Enter password 1: ')
    password_1 = 'abciabci..'
    #password_2 = input('Enter password 2: ')
    password_2 = '..,,..,,'
    return(username, password_1, password_2)

def enter_login_information(browser_object, username, password_1, password_2):
    username_field = browser_object.find_element_by_css_selector('#username')
    username_field.send_keys(username)
    password_1_field = browser_object.find_element_by_css_selector('#password')
    password_1_field.send_keys(password_1)
    login_button = browser_object.find_element_by_id("login_btn")
    login_button.click()
    add_time_delay(5)
    try:
        password_2_field = browser_object.find_element_by_css_selector('#password')
        password_2_field.send_keys(password_2)
        unlock_button = browser_object.find_element_by_id("unlock_btn")
        unlock_button.click()
    except:
        raise ValueError('The password_2 login failed')

def get_recipient_email_address(): # Perhaps add default to test other functtionality
    recipient_email_address = sys.argv[2]
    return recipient_email_address

def get_message_string():
    message_string = sys.argv[2:]
    return message_string

def open_new_message(browser_object):
    compose_button = ''
    while True:
        try:
            compose_button = browser_object.find_element_by_css_selector('.compose')
            break
        except:
            print('Waiting for page to load')
            add_time_delay(2)
    compose_button.click()


def write_message(browser_object, recipient_email_address, message_string):
    while True:
        try:
            to_field = browser_object.switch_to_active_element()
            to_field.send_keys(recipient_email_address)
            break

        except:
            print('Waiting for new message to load')
            add_time_delay(2)

def click_send_email(browser_object):
    click_send_email_button = browser_object.find_element_by_css_selector("button.mobileFull:nth-child(4)")
    click_send_email_button.click()
    

#Engine
    
#recipient_email_address = get_recipient_email_address(sys.argv) # Perhaps add default to test other functtionality
recipient_email_address = '000td000@gmail.com'
#message_string = get_message_string(sys.argv)
username, password_1, password_2 = get_login_input()
message_string = 'test test test 123 test'
browser_object = get_browser_object()
load_webpage(browser_object)
enter_login_information(browser_object, username, password_1, password_2)
add_time_delay(4)
open_new_message(browser_object)
write_message(browser_object, recipient_email_address, message_string)
click_send_email(browser_object)
