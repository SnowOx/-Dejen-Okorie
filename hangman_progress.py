#! python3
# hangman_game.py

# Begin by creating a hangman game for a human guesser.
# # Would like to create a more sophisticated GUI after I have completed the basic mechanics

import random

TEXT_FILE_LOCATION = "english_words.txt"

with open(TEXT_FILE_LOCATION) as open_file:
    english_words = open_file.read().splitlines()

def pick_random_hidden_word(english_words):
    hidden_word = random.choice(english_words)
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
    for letter_and_marker_pair in hidden_letter_and_marker_list:
        for k, v in letter_and_marker_pair.items():
            if v is 1:
                print(' ' + str(k) + ' ', end='')
            if v is 0:
                print(' ' + '*' + ' ', end='')

def get_letter_guess(hidden_letter_and_marker_list):
    letter_guess = input('Enter a letter to guess >> ').upper()
    for letter_and_marker_pair in hidden_letter_and_marker_list:
        for k, v in letter_and_marker_pair.items():
            if (k in letter_and_marker_pair) and (v in letter_and_marker_pair == 1):
                print('You have already guessed this letter. Guess again')
                get_letter_guess(hidden_letter_and_marker_list)
    return letter_guess

def     check_guess_and_update(letter_guess, hidden_letter_and_marker_list):
    for letter_and_marker_pair in hidden_letter_and_marker_list:
        for k in letter_and_marker_pair.keys():
            if k == letter_guess:
                letter_and_marker_pair[k] = 1
                print('DEBUG: Correct guess')
            elif k != letter_guess:
                print('Incorrect guess')

def check_whether_game_complete(hidden_letter_and_marker_list, hidden_word_length):
    game_progress_counter = 0
    for letter_and_marker_pair in hidden_letter_and_marker_list:
        for v in letter_and_marker_pair.values():
            if v is 1:
                game_progress_counter += 1
    if game_progress_counter == hidden_word_length:
        game_finished = True
    else:
        game_finished = False
    return game_finished

def show_end_of_game_congratulations(hidden_word):
    print('\nCongratulations. You guessed the hidden word %s' % hidden_word)

# Engine

def play_hangman_game():
    hidden_word = pick_random_hidden_word(english_words)
    print(hidden_word)
    hidden_word_length = get_hidden_word_length(hidden_word)
    hidden_letter_and_marker_list = generate_hidden_letter_and_marker_list(hidden_word)
    #print(hidden_letter_and_marker_list) DBUGto remove
    game_finished = False
    while game_finished != True:
        letter_guess = get_letter_guess(hidden_letter_and_marker_list)
        check_guess_and_update(letter_guess, hidden_letter_and_marker_list)
        print_hidden_letter_and_marker_list(hidden_letter_and_marker_list)
        game_finished = check_whether_game_complete(hidden_letter_and_marker_list, hidden_word_length)
        #print(hidden_letter_and_marker_list) DBUGto remove
        print('Game finished = ' + str(game_finished))
    show_end_of_game_congratulations(hidden_word)
    #print(hidden_letter_and_marker_list) DBUG to remove

play_hangman_game()

# Make this work before expanding game
