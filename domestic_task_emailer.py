#! python3
# domestic_task_emailer.py

import smtplib
import random
import datetime

def select_domestic_task():
    selected_task = random.choice(domestic_tasks)
    domestic_tasks.remove(selected_task)
    return selected_task

def connect_to_smtp_server(server_address, server_port,
                           sender_account_email, sender_account_password):
    smtp_object = smtplib.SMTP(server_address, server_port)
    smtp_object.ehlo()
    smtp_object.starttls()
    smtp_object.login(sender_account_email, sender_account_password)
    return smtp_object

def get_current_time():
    current_time = datetime.datetime.now().strftime('%H:%M on the %d/%m/%Y')
    return current_time

def send_message(sender_account_email,
                 recipient_email, person_name,
                 selected_domestic_task, smtp_object, current_time):
    smtp_object.sendmail(sender_account_email, recipient_email,
                         'Subject: Weekly Domestic Task for %s\n\n\
                          Dear %s, \n\
                          Your task for this week is %s\n\
                          Best wishes,\n\
                          T\n\n\
                          P.S The current time is %s\n' % (
            person_name, person_name, selected_domestic_task, current_time))

def quit_server_connection(smtp_object):
    smtp_object.quit()

def assign_domestic_tasks_and_send_emails(people,
                                          server_address, server_port,
                                          sender_account_email, sender_account_password,
                                          recipient_email):
    for person_name in people:
        selected_domestic_task = select_domestic_task()
        smtp_object = connect_to_smtp_server(server_address, server_port,
                                             sender_account_email,
                                             sender_account_password)
        current_time = get_current_time()
        send_message(sender_account_email, recipient_email,
                     person_name, selected_domestic_task, smtp_object,
                     current_time)
        quit_server_connection(smtp_object)


# Engine
domestic_tasks = ['washing the dishes',
                  'cleaning the  bathroom',
                  'vacuuming Fubin\'s room',
                  'walking all of the neighbourhood\'s dogs']

people = ['Robert', 'Mica', 'Lina', 'Keith']
sender_account_email = '000td000@gmail.com'
recipient_email = '1239@pm.me'
server_address = 'smtp.gmail.com'
server_port = 587
sender_account_password = input('Enter password >> ')
assign_domestic_tasks_and_send_emails(people,server_address,
                                      server_port,sender_account_email,
                                      sender_account_password, recipient_email)

# Solved
