#! python3
# hangman_game.py

Import random

def random_word_picker()
	hidden_word = #english_word_array#[random.randint(1, #number of words in dictionary#)]
	hidden_word_length = len(hidden_word_length)
	return (hidden_word, hidden_word_length)

def generate_dictionary_for_word_length(hidden_word):
	hidden_word_record = {0: letter for letter in hidden_word}
	return hidden_word_record

def print_hidden_word_record:
	for k,v in hidden_word_record.items():
		if k == 0:
			print(‘ ‘ + v + ‘ ‘,end=’’)
		if k == 1:
			print(‘ ‘ + ‘_’ + ‘ ‘,end=’’)


english_alphabet = [‘a’, ‘b’, ‘c’, ’d’, ’e’, ’f’, ’g’, ‘h’, ‘i’, ‘j’, 
                    ‘k’, ‘l’, ‘m’, ‘n’, ‘o’, ‘p’, ‘q’, ‘r’, ‘s’, ‘t’, 
                    ‘u’, ‘v’, ‘w’, ‘x’, ‘y’, ‘z’]

def computer_guess_letter(english_alphabet):
	letter_guess = random.choice(english_alphabet)
	english_alphabet.pop(letter_guess)
	
def computer_check_possible_words():
	
# Todo: computer checks all words of hidden_word_length in #english_word_array#
	For words in #english_word_array#:
