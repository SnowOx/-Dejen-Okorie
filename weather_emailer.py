#! python3
# weather_emailer.py

from bs4 import BeautifulSoup
import requests
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Could customise this script to add a preferred location for ech person,
# to search the site for the weather in their location, and to send them their preferred weather


def get_weather_requests_page_object():
    test_the_url = requests.get(WEATHER_FORECASTER_URL)
    test_the_url.raise_for_status()
    weather_requests_page_object = requests.get(WEATHER_FORECASTER_URL).content
    return weather_requests_page_object


def get_weather_page_soup(requests_page_object):
    soup = BeautifulSoup(requests_page_object, "lxml")
    return soup


def get_day_temperature(soup):
    day_temp_class = soup.find(class_="dayTemp")
    day_temperature = day_temp_class['data-value-raw']
    print(day_temperature)
    return day_temperature


def get_chance_of_rain(soup):
    chance_of_rain_uncleaned = soup.find(title="Chance of precipitation").get_text()
    chance_of_rain = chance_of_rain_uncleaned[:4]
    return chance_of_rain

def get_general_weather_comment(soup): ###
    general_weather_comment_class = soup.find(class_="icon wx")
    general_weather_comment = general_weather_comment_class['title']
    return general_weather_comment


def get_sun_time_moon_phases_air_pollution_pollen_count(soup):
    sun_moon_phase_information_raw = soup.find(class_="sunHolder").get_text()
    sun_moon_phase_information_cleaned_once = sun_moon_phase_information_raw.split('\n')
    sun_moon_phase_information_cleaned_twice = [x for x in sun_moon_phase_information_cleaned_once if x != '']
    return sun_moon_phase_information_cleaned_twice


def get_browser_object():
    print('Thank you for the information. Now loading Firefox Browser')
    browser_object = webdriver.Firefox()
    return browser_object


def load_webpage(browser_object):
    browser_object.get(WEBPAGE)


def add_time_delay(seconds):
    time.sleep(int(seconds))


def get_login_input():
    username = input('Enter username')
    password_1 = input('Enter password 1: ')
    password_2 = input('Enter password 2: ')
    return(username, password_1, password_2)


def enter_login_information(browser_object):
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
    to_field.send_keys(RECIPIENT_EMAIL_ADDRESS, Keys.TAB)
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

def print_confirmation():
    print('Message sent to %s !' % RECIPIENT_EMAIL_ADDRESS)


# Engine

weather_requests_page_object = get_weather_requests_page_object()
weather_soup = get_weather_page_soup(weather_requests_page_object)
day_temperature = get_day_temperature(weather_soup)
chance_of_rain = get_chance_of_rain(weather_soup)
general_weather_comment = get_general_weather_comment(weather_soup)
sun_time_moon_phases_air_pollution_pollen_count = get_sun_time_moon_phases_air_pollution_pollen_count(weather_soup)

BODY_TEXT = input(f'Chance of rain = {chance_of_rain}\nGeneral Weather Comment = {general_weather_comment}\n' +
'Day temperature = {day_temperature}\n{sun_time_moon_phases_air_pollution_pollen_count}\n')
RECIPIENT_EMAIL_ADDRESS = input('Enter recipient\'s email address:\n')
RECIPIENT_EMAIL_ADDRESSES = ('000td000@gmail.com', '1239@pm.me')
WEATHER_FORECASTER_URL = "https://www.metoffice.gov.uk/public/weather/forecast/gcpvg"
WEBPAGE = 'https://mail.protonmail.com/login'
SUBJECT = 'Daily Weather'


username, password_1, password_2 = get_login_input()
browser_object = get_browser_object()
load_webpage(browser_object)
enter_login_information(browser_object)
add_time_delay(4)
open_new_message(browser_object)
write_message(browser_object)
