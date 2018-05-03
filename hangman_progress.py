#! python3
# hangman_game.py

# Begin by creating a hangman game for a human guesser.

import random

english_words = #

def pick_random_hidden_word(english_words)
	hidden_word = english_words[random.randint(1, len(english_words))]
	hidden_word_length = len(hidden_word_length)
	return (hidden_word, hidden_word_length)

def generate_guess_record_for_word_length(hidden_word): # Modify this to order the stored letters
	hidden_word_record = {0: letter for letter in hidden_word}
    return hidden_word_record
	
def print_hidden_word_record():
	for k,v in hidden_word_record.items():
		if k == 1:
			print(‘ ‘ + str(v) + ‘ ‘, end=’’)
		if k == 0:
			print(‘ ‘ + ‘_’ + ‘ ‘, end=’’)

def user_guess():
	letter_guess = input(‘Enter a letter to guess’)
	return letter_guess

def check_guess_and_update(letter_guess):
	for k, v in hidden_word_record.items():
    if v == letter_guess:
	    hidden_word_record[v] = 1
    elif v != letter_gueass
        print(‘Incorrect guess’)	

def process_user_guesses_and_update_guess_record()
	while v ==  0 in hidden_word_record.values():
        print_hidden_word_record()
        letter_guess = user_guess()
        check_guess_and_update(letter_guess)
    game_outcome = 'win'
	return game_outcome = 'win' 
	
 def show_end_of_game_result(game_outcome, hidden_word):
	if game_outcome == 'win':
		print(‘Congratulations. You guessed the hidden word %s’ % hidden_word)
		
def play_hangman_game()
    hidden_word, hidden_word_length = pick_random_hidden_word(english_words)
    generate_guess_record_for_word_length(hidden_word)
    game_outcome = process_user_guesses_and_update_guess_record
    show_end_of_game_result(game_outcome, hidden_word)

play_hangman_game()

# Make this work before expanding game

		

	
