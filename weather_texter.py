#! python3
# weather_texter.py

from bs4 import BeautifulSoup
import requests
from datetime import datetime
from twilio.rest import Client
import time

# Could customise this script to add a preferred location for ech person,
# to search the site for the weather in their location, and to send them their preferred weather


ACCOUNT_SID = '#'
AUTHORISATION_TOKEN = '#'
TWILIO_CLIENT = Client(ACCOUNT_SID, AUTHORISATION_TOKEN)
MY_TWILIO_NUMBER = '#'
WEATHER_FORECASTER_URL = "https://www.metoffice.gov.uk/public/weather/forecast/##"


def get_current_date_and_time_string():
    date_and_time = datetime.fromtimestamp(time.time())
    formatted_date_and_time  = date_and_time.strftime("%A %d %B %Y at %H:%M:%S")
    return formatted_date_and_time


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
    return day_temperature


def get_chance_of_rain(soup):
    chance_of_rain_uncleaned = soup.find(title="Chance of precipitation").get_text()
    chance_of_rain = chance_of_rain_uncleaned[:4].strip()
    return chance_of_rain


def get_general_weather_comment(soup):
    general_weather_comment_class = soup.find(class_="icon wx")
    general_weather_comment = general_weather_comment_class['title']
    return general_weather_comment


def get_sun_time_moon_phases_air_pollution_pollen_count(soup):
    sun_moon_phase_information_raw = soup.find(class_="sunHolder").get_text()
    sun_moon_phase_information_cleaned_once = sun_moon_phase_information_raw.split('\n')
    sunrise_time = sun_moon_phase_information_cleaned_once[3]
    sunset_time = sun_moon_phase_information_cleaned_once[5]
    moon_phase = sun_moon_phase_information_cleaned_once[6]
    air_pollution = sun_moon_phase_information_cleaned_once[8] + ' ' + sun_moon_phase_information_cleaned_once[9]
    pollen_count = sun_moon_phase_information_cleaned_once[10] + ' ' + sun_moon_phase_information_cleaned_once[11]
    return (sunrise_time, sunset_time, moon_phase, air_pollution, pollen_count)


def send_text_message_to_number(body_text, recipient_number):
    text_message = TWILIO_CLIENT.messages.create(body=body_text, from_=MY_TWILIO_NUMBER, to=recipient_number)
    print('Sending message from %s to %s' % (MY_TWILIO_NUMBER, recipient_number))


# Engine
formatted_date_and_time = get_current_date_and_time_string()
weather_requests_page_object = get_weather_requests_page_object()
weather_soup = get_weather_page_soup(weather_requests_page_object)
day_temperature = get_day_temperature(weather_soup)
chance_of_rain = get_chance_of_rain(weather_soup)
general_weather_comment = get_general_weather_comment(weather_soup)
sunrise_time, sunset_time, moon_phase, air_pollution, pollen_count = get_sun_time_moon_phases_air_pollution_pollen_count(weather_soup)
body_text = f'''Daily Weather on {formatted_date_and_time} >>
General comment: The weather is {general_weather_comment}
Chance of rain: {chance_of_rain} %
Day temperature: {day_temperature}
{sunrise_time}
{sunset_time}
{moon_phase}
{air_pollution}
{pollen_count}
'''
print(body_text)
telephone_number_of_recipient = '#'
send_text_message_to_number(body_text, telephone_number_of_recipient)
