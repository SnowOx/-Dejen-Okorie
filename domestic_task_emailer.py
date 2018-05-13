#! python3
# domestic_task_emailer.py

import smtplib
import random
import datetime

DOMESTIC_TASKS = ['washing the dishes',
                  'cleaning the  bathroom',
                  'vacuuming Fubin\'s room',
                  'walking all of the neighbourhood\'s dogs']

PEOPLE = ['Robert', 'Mica', 'Lina', 'Keith']
SENDER_EMAIL = '000td000@gmail.com'
RECIP_EMAIL = '1239@pm.me'
SERVER_ADDRESS = 'smtp.gmail.com'
SERVER_PORT = 587
SENDER_PASSWORD = input('Enter password >> ')

def select_domestic_task():
    selected_task = random.choice(DOMESTIC_TASKS)
    DOMESTIC_TASKS.remove(selected_task)
    return selected_task

def connect_to_smtp_server():
    smtp_object = smtplib.SMTP(SERVER_ADDRESS, SERVER_PORT)
    smtp_object.ehlo()
    smtp_object.starttls()
    smtp_object.login(SENDER_EMAIL, SENDER_PASSWORD)
    return smtp_object

def get_current_time():
    current_time = datetime.datetime.now().strftime('%H:%M on the %d/%m/%Y')
    return current_time

def send_message(smtp_object, person_name, selected_domestic_task, current_time):
    smtp_object.sendmail(SENDER_EMAIL, RECIP_EMAIL,'Subject: Weekly Domestic Task for %s\n\n' % person_name+
                          'Dear %s, \n' % person_name +
                          'Your task for this week is %s\n' % selected_domestic_task +
                          'Best wishes,\n'+
                          'T\n\n'+
                          'P.S The current time is %s\n' % current_time)

def quit_server_connection(smtp_object):
    smtp_object.quit()

def assign_domestic_tasks_and_send_emails():
    for person_name in PEOPLE:
        selected_domestic_task = select_domestic_task()
        smtp_object = connect_to_smtp_server()
        current_time = get_current_time()
        send_message(smtp_object, person_name,selected_domestic_task, current_time)
        quit_server_connection(smtp_object)


# Engine


assign_domestic_tasks_and_send_emails()

# Solved
