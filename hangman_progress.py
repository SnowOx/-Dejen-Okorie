#! python3
# hangman_game.py

# Begin by creating a hangman game for a human guesser.

import random

english_words = ['pear', 'apple']

def pick_random_hidden_word(english_words):
    hidden_word = random.choice(english_words)
    hidden_word_length = len(hidden_word)
    return hidden_word


def get_hidden_word_length(hidden_word):
    hidden_word_length = len(hidden_word)
    return hidden_word_length


def generate_hidden_letter_and_marker_list(hidden_word):
    hidden_letter_and_marker_list = []
    for letter in hidden_word:
        some_dict = {}
        some_dict[letter] = 0
        hidden_letter_and_marker_list.append(some_dict)
    return hidden_letter_and_marker_list


def print_hidden_letter_and_marker_list(hidden_letter_and_marker_list):
    for letter_and_marker_dictionary in hidden_letter_and_marker_list:
        for k, v in letter_and_marker_dictionary.items():
            if v is 1:
                print(' '+ str(k) + ' ', end='')
            if v is 0:
                print(' ' + '*' + ' ', end='')


def get_letter_guess():
    letter_guess = input('Enter a letter to guess >> ')
    return letter_guess


def check_guess_and_update(letter_guess, hidden_letter_and_marker_list):
    for letter_and_marker_dict in hidden_letter_and_marker_list:
        for k in letter_and_marker_dict.keys():
            if k is letter_guess:
                letter_and_marker_dict[k] = 1
                print('DEBUG: Correct guess')
            elif k is not letter_guess:
                print('Incorrect guess')


def check_whether_game_complete(hidden_letter_and_marker_list, hidden_word_length):
    game_progress_counter = 0
    for letter_and_marker_dictionary in hidden_letter_and_marker_list:
        for v in letter_and_marker_dictionary.values():
            if v is 1:
                game_progress_counter += 1
    if hidden_word_length is not game_progress_counter:
        game_progress = 'game incomplete'
        return game_progress
    else:
        return

                
def process_user_guesses_and_update_guess_record(hidden_letter_and_marker_list, letter_guess, hidden_word_length):
 
    return

	
def show_end_of_game_result(hidden_word):
    print('Congratulations. You guessed the hidden word %s' % hidden_word)

		
def play_hangman_game():
    hidden_word = pick_random_hidden_word(english_words)
    print(hidden_word)
    hidden_word_length = get_hidden_word_length(hidden_word)
    print(hidden_word_length)
    hidden_letter_and_marker_list = generate_hidden_letter_and_marker_list(hidden_word)
    print(hidden_letter_and_marker_list)
    while True:
        letter_guess = get_letter_guess()
        print(letter_guess)
        check_guess_and_update(letter_guess, hidden_letter_and_marker_list)
        print(hidden_letter_and_marker_list)
        game_progress = check_whether_game_complete(hidden_letter_and_marker_list,
                                                    hidden_word_length)
        print(game_progress)
        check_whether_game_complete(hidden_letter_and_marker_list, hidden_word_length)
        print_hidden_letter_and_marker_list(hidden_letter_and_marker_list)
        check_guess_and_update(letter_guess, hidden_letter_and_marker_list)
        
    #show_end_of_game_result(hidden_word)

play_hangman_game()

# Make this work before expanding game
