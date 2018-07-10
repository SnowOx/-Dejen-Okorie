#! python3
# looking_busy.py

import pyautogui
import time

def nudge_mouse()
    pyautogui.moveRel(10,10)

def time_delay(seconds)
    time.sleep(seconds)
    
#Engine
while True:
    nudge_mouse()
    time_delay(10)
    
