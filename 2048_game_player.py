#!python3
# 2048_game_player.py

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

SITE = 'https://gabrielecirulli.github.io/2048/'

def launch_browser_and_get_browser_object():
    browser_object = webdriver.Firefox()
    print(type(browser_object))
    browser_object.get('https://gabrielecirulli.github.io/2048/')
    return browser_object

def click_new_game_button(browser_object):
    try:
        new_game_button = browser_object.find_element_by_class_name("restart-button")
        print('Found the tag with the text %s' % new_game_button.text)
        new_game_button.click()        
    except:
        print('Did not find the element to start a new game')

def get_page_element(browser_object):
    page_element = browser_object.find_element_by_tag_name('html')
    return page_element

def check_game_progress(browser_object):
    try:
        browser_object.find_element_by_class_name("game-message.game-over")
        return True
    except:
        print('Still playing')
        return False

def get_game_score(browser_object):
    game_score_container = browser_object.find_element_by_class_name("score-container")
    game_score = game_score_container.text
    print('Game over. The 2048 score was %s !' % str(game_score))
    return game_score
    
    
def send_key_presses_to_page_element(page_element):
        page_element.send_keys(Keys.UP)
        page_element.send_keys(Keys.RIGHT)
        page_element.send_keys(Keys.DOWN)
        page_element.send_keys(Keys.LEFT)

def play_game_until_complete():
    browser_object = launch_browser_and_get_browser_object()
    click_new_game_button(browser_object)
    page_element = get_page_element(browser_object)
    game_over = False
    while not game_over:
        send_key_presses_to_page_element(page_element)
        game_over = check_game_progress(browser_object)
    game_score = get_game_score(browser_object)

#def play_again() 

# Engine

play_game_until_complete()

