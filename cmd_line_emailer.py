#! python3
# cmd_line_emailer.py

import time
import sys
from selenium import webdriver

def get_browser_object():
    browser_object = webdriver.Firefox()
    return browser_object

def load_webpage(browser_object, webpage):
    browser_object.get(webpage)

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
    #password_2_field = browser_object.find_element_by_css_selector(  # )
    #password_1_field.send_keys(password_1)

#def get_recipient_email_address(sys.argv):
#    recipient_email_address = sys.argv[2]
#    return recipient_email_address

#def get_message_string(sys.argv):
#    message_string = sys.argv[2:]
#    return message_string

#def send_email

username = '1239'
password_1 = input('Enter pw1')
enter_login_information(username, password_1,password_2, browser_object)