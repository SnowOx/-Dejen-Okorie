#! python3
# cmd_line_emailer.py

import time
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def get_browser_object():
    browser_object = webdriver.Firefox()
    return browser_object


def load_webpage(browser_object):
    browser_object.get(WEBPAGE)


def add_time_delay(seconds):
    time.sleep(int(seconds))


def get_login_input():
    username = # Enter protonmail username
    password_1 = sys.argv[1]
    password_2 = sys.argv[2]
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


def get_recipient_email_address():
    recipient_email_address = sys.argv[3]
    return recipient_email_address


def get_message_string():
    message_string = sys.argv[4]
    return message_string


def open_new_message(browser_object):
    while True:
        try:
            compose_button = browser_object.find_element_by_css_selector('.compose')
            break
        except:
            print('Waiting for page to load')
            add_time_delay(2)
    compose_button.click()


def write_message(browser_object):
    add_time_delay(2)
    add_recipient_address(browser_object)
    add_subject(browser_object)
    add_body_text(browser_object)
    send_email(browser_object)


def add_recipient_address(browser_object):
    to_field = browser_object.switch_to_active_element()
    to_field.send_keys(recipient_email_address, Keys.TAB)
    to_field.send_keys(Keys.TAB)


def add_subject(browser_object):
    subject_field = browser_object.switch_to_active_element()
    subject_field.send_keys(SUBJECT)
    subject_field.send_keys(Keys.TAB)
    add_time_delay(2)


def add_body_text(browser_object):
    body_field = browser_object.switch_to_active_element()
    body_field.send_keys(Keys.CONTROL + "a")
    body_field.send_keys(Keys.DELETE)
    body_field.send_keys(BODY_TEXT)
    body_field.send_keys(Keys.TAB * 6)
    add_time_delay(1)


def send_email(browser_object):
    send_button = browser_object.switch_to_active_element()
    send_button.click()


# Engine

WEBPAGE = 'https://mail.protonmail.com/login'
BODY_TEXT = get_message_string()
recipient_email_address = get_recipient_email_address()
username, password_1, password_2 = get_login_input()
SUBJECT = ('Message from %s!' % username)
browser_object = get_browser_object()
load_webpage(browser_object)
enter_login_information(browser_object, username, password_1, password_2)
add_time_delay(4)
open_new_message(browser_object)
write_message(browser_object)

#Solved!
