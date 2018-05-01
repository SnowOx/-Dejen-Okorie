#	computer guess process:
#	computer guesses a letter at random
#	if hit, computer guesses any letter within the words in list that contain that letter in that location
#	if there are only a few words left, the computer guesses the word

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
    elif v != letter_guess
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
	
# Todo: add limited number of guesses

#english_alphabet = [‘a’, ‘b’, ‘c’, ’d’, ’e’, ’f’, ’g’, ‘h’, ‘i’, ‘j’, ‘k’, ‘l’, ‘m’, ‘n’, ‘o’, ‘p’, ‘q’, ‘r’, ‘s’, ‘t’, ‘u’, ‘v’, ‘w’, ‘x’, ‘y’, ‘z’]

#def computer_guess_letter(english_alphabet):
#	letter_guess = random.choice(english_alphabet = [‘a’, ‘b’, ‘c’, ’d’, ’e’, ’f’, ’g’, ‘h’, ‘i’, ‘j’, ‘k’, ‘l’, ‘m’, ‘n’, ‘o’, ‘p’, ‘q’, ‘r’, ‘s’, ‘t’, ‘u’, ‘v’, ‘w’, ‘x’, ‘y’, ‘z’]
#	english_alphabet.pop(letter_guess)

#def computer_check_possible_words():
	
#def get_possible_guesses()
#	for possible_word in english_words:
#		word_letters = word.split()
		

	
