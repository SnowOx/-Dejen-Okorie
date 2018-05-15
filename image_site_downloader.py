#! python3
# image_site_downloader.py

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

SITE = 'https://unsplash.com/'
DESIRED_SEARCH_TERM = "leaf"

def open_browser_and_get_browser_object():
    global browser_object
    browser_object = webdriver.Firefox()
    print(type(browser_object))
    browser_object.get(SITE)
    return browser_object

def get_search_bar_object_and_search(DESIRED_SEARCH_TERM):
    search_bar_object = browser_object.find_element_by_class("qWUF0")
    search_bar_object.send_keys(DESIRED_SEARCH_TERM)
    search_button_object = browser_object.find_element_by_class("_37zTg _1l4Hh _1CBrG _3TTOE Sb388")
    search_button_object.click()


browser_object = open_browser_and_get_browser_object()
get_search_bar_object_and_search(DESIRED_SEARCH_TERM)