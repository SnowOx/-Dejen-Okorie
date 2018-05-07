#! python3
# cardGuessGame.py

import random

def generate_hidden_card():
    hidden_card = random.randint(1, 52)
    return hidden_card

def get_human_guess():
    human_guess = int(input('Please enter your guess: '))
    return human_guess

def add_human_guess_to_dictionary(human_guess, guess_relation_to_hidden_card):
    human_guesses_dict[human_guess] = guess_relation_to_hidden_card

def check_guess_against_hidden_card(hidden_card, guess):
    if guess == hidden_card:
        print('Correct')
        guess_relation_to_hidden_card = 'guessed'
        return guess_relation_to_hidden_card
    if guess < hidden_card:
        print('Incorrect. Your guess was lower than the hidden card')
        #options_list.pop[i:] I could use this as part of an options list approach where there is an initial list that
        # contains all of the options that the hidden card might be. I then remove numbers from the options list depending on
        # the check_guess_against_hidden_card result. Suggest writing this options list variant afterwards.
        guess_relation_to_hidden_card = 'hidden card is higher'
        return guess_relation_to_hidden_card
    if guess > hidden_card:
        print('Incorrect. Your guess was higher than the hidden card')
        guess_relation_to_hidden_card = 'hidden card is lower'
        return guess_relation_to_hidden_card

def generate_computer_guess():
    return random.randint(1, 52)

def check_computer_guess_against_all_previous_guesses(computer_guess):
    if not computer_guesses_dict or human_guesses_dict:
        return 'valid guess'
    
    for previous_computer_guess, previous_computer_guess_relation_to_hidden_card in computer_guesses_dict.items():
        if computer_guess == previous_computer_guess:
            return 'invalid guess'
        if computer_guess > previous_computer_guess and previous_computer_guess_relation_to_hidden_card == 'hidden card is lower':
            return 'invalid guess'
        if computer_guess < previous_computer_guess and previous_computer_guess_relation_to_hidden_card == 'hidden card is higher':
            return 'invalid guess'
        
    for previous_human_guess, previous_human_guess_relation_to_hidden_card in human_guesses_dict.items():
        if computer_guess == previous_human_guess:
            return 'invalid guess'
        if computer_guess > previous_human_guess and previous_human_guess_relation_to_hidden_card == 'hidden card is lower':
            return 'invalid guess'
        if computer_guess > previous_human_guess and previous_human_guess_relation_to_hidden_card == 'hidden card is higher':
            print('human_guesses relation' + str(human_guesses_dict[guess_relation_to_hidden_card]))
            return 'invalid guess'
    return 'valid guess'
            
def add_computer_guess_to_dictionary(computer_guess, guess_relation_to_hidden_card):
    computer_guesses_dict[computer_guess] = guess_relation_to_hidden_card

    

## Engine
computer_guesses_dict = {}
human_guesses_dict = {}
hidden_card = generate_hidden_card()
print('DBUG hidden_card =' + str(hidden_card))

while True:  
    computer_guess = generate_computer_guess()
    print('DBUG computer_guess =' + str(computer_guess))
    guess_status = check_computer_guess_against_all_previous_guesses(computer_guess)
    if guess_status == 'invalid guess':
        continue
    print('DBUG guess status =' + str(guess_status))
    guess_relation_to_hidden_card = check_guess_against_hidden_card(hidden_card, computer_guess)
    add_computer_guess_to_dictionary(computer_guess, guess_relation_to_hidden_card)
    print('DBUG computer_guesses_dict = ' + str(computer_guesses_dict))
    if guess_relation_to_hidden_card == 'guessed':
        break


# Todo: Add the working human guess mechanism (below) to the game           
##    human_guess = get_human_guess()
##    guess_relation_to_hidden_card = check_guess_against_hidden_card(hidden_card,human_guess)
##    add_human_guess_to_dictionary(human_guess, guess_relation_to_hidden_card)
##    if guess_relation_to_hidden_card == 'guessed':
##        break
##    get_valid_computer_guess():



    
print('Complete')


    



