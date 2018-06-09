#! python3
# hangman_game.py

# Begin by creating a hangman game for a human guesser.
# # Would like to create a GUI after I have completed the basic mechanics
"""
  _ _ _ _
  |     |
  |   \ O /
  |     |
  |    / \
 _^_ _
"""

import random
#import requests
#import bs4

TEXT_FILE_LOCATION = "E:\\Google Drive\\OP2\\dk\\english_words.txt"

def pick_random_hidden_word(english_words):
    hidden_word = random.choice(english_words)
    return hidden_word


def get_hidden_word_length(hidden_word):
    hidden_word_length = len(hidden_word)
    return hidden_word_length


def generate_hidden_letters_and_markers_for(hidden_word):
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
    print()


def get_letter_guess(letter_guess_record):
    letter_guess = input('Enter a letter to guess, or enter * for a clue>> ').upper()
    if letter_guess == '*':
        show_clue(hidden_word)
        get_letter_guess(letter_guess_record)
    elif letter_guess in letter_guess_record:
        print('You have already guessed this letter. Please guess again!')
        get_letter_guess(letter_guess_record)
    return letter_guess


def show_clue(hidden_word):
    clue_page_request = requests.get(
        'https://www.wordwebonline.com/search.pl?w=' + hidden_word)
    clue_page_request.raise_for_status()
    clue_page = bs4.BeautifulSoup(clue_page_request)
    clue_page_elements = clue_page.select('span [class="def"]')
    clue = clue_page_elements[0].getText()
    print('The clue is:\n%s' % clue)


def create_letter_guess_records():
    letter_guess_record = []
    number_of_guesses_record = 0
    return (letter_guess_record, number_of_guesses_record)


def update_letter_guess_records(letter_guess, letter_guess_record, number_of_guesses_record):
    letter_guess_record.append(letter_guess)
    number_of_guesses_record += 1
    return (letter_guess_record, number_of_guesses_record)

hangman_image =
['  _ _ _ _  '],
[' |     |   '],
[' |   \ O / '],
[' |     |   '],
[' |    / \  '],
[' _^_ _     '],


def check_guess_and_update(letter_guess, hidden_letter_and_marker_list):
    correct_or_incorrect_guess_counter = 0
    for letter_and_marker_pair in hidden_letter_and_marker_list:
        for k in letter_and_marker_pair.keys():
            if k == letter_guess:
                letter_and_marker_pair[k] = 1
                correct_or_incorrect_guess_counter += 1
    show_correct_or_incorrect_message_for_the_guess(correct_or_incorrect_guess_counter, letter_guess)


def show_correct_or_incorrect_message_for_the_guess(correct_or_incorrect_guess_counter, letter_guess):
    if correct_or_incorrect_guess_counter > 0:
        print('Correct! The letter %s appears in the word' % letter_guess)
    else:
        print('Incorrect! The letter %s does not appear in the word' % letter_guess)


def check_whether_game_complete(hidden_letter_and_marker_list, hidden_word_length):
    game_progress_counter = 0
    for letter_and_marker_pair in hidden_letter_and_marker_list:
        for v in letter_and_marker_pair.values():
            if v is 1:
                game_progress_counter += 1
    if game_progress_counter == hidden_word_length:
        is_game_finished = True
    else:
        is_game_finished = False
    return is_game_finished


def show_end_of_game_congratulations(hidden_word):
    print('\nCongratulations! You guessed the hidden word \'%s\'!' % hidden_word.title())


def main_game_loop(is_game_finished, hidden_letter_and_marker_list, hidden_word_length):
    letter_guess_record, number_of_guesses_record = create_letter_guess_records()
    while is_game_finished != True:
        letter_guess = get_letter_guess(letter_guess_record)
        update_letter_guess_records(letter_guess, letter_guess_record, number_of_guesses_record)
        check_guess_and_update(letter_guess, hidden_letter_and_marker_list)
        print_hidden_letter_and_marker_list(hidden_letter_and_marker_list)
        is_game_finished = check_whether_game_complete(hidden_letter_and_marker_list, hidden_word_length)


def play_hangman_game():
    hidden_word = pick_random_hidden_word(english_words)
    print(hidden_word)  # DBUG To remove
    hidden_word_length = get_hidden_word_length(hidden_word)
    hidden_letter_and_marker_list = generate_hidden_letters_and_markers_for(hidden_word)
    is_game_finished = False
    main_game_loop(is_game_finished, hidden_letter_and_marker_list, hidden_word_length)
    show_end_of_game_congratulations(hidden_word)


# Engine
with open(TEXT_FILE_LOCATION) as open_file:
    english_words = open_file.read().splitlines()  # capitalise english_words ?
play_hangman_game()
