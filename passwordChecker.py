#! python3
# passWordChecker.py - Program to check if password contains
# at least 1 upper and lower case character, at least 8 characters,
# and at least 1 digit

import re
import time

# user password input


def pwordChecker(password):
    regex1 = re.compile(r'[A-Z]+[a-z]+[0-9]+')
    regex2 = re.compile(r'\w{8,}')# Question: why does this regex need to be on its own line? Adding it to the above means that .search() does not return True
    
    check1 = regex1.search(password)
    check2 = regex2.search(password)

    print('%s -- %s' % (check1, check2))

    if check1 and check2:
        print('Check passed. \nThe password \'%s\' is adequate.\n' % password)
    else:
        print('Check failed. \nThe password \'%s\' is inadequate\n' % password)

#password = str(input('Please enter the password to test'))
passwordList = ['oneone', 'oneoneone', 'oneonefFffwfewweefe1', 'Not8', 'Oneoneone1', 'f']

# Ask for human imput or use text bank 

password = input('Please enter password to be checked >> ')
if password:
    pwordChecker(password)
    
else:
    print('No password entered. Using test bank instead in two seconds...')
    time.sleep(2)
    for password in passwordList:
        pwordChecker(password)

print('\nDone')  # Solved!
