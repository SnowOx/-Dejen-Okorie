#! python3
# hangman_game.py

# Begin by creating a hangman game for a human guesser.
# # Would like to create a GUI after I have completed the basic mechanics


# There is a bug whereby, after a clue has ben given, the next guess is taken to be '*' rather than the entered guess letter
# Solved the bug. I had been running the get_letter_guess function wihtout assigning its return value to
# overwrite the letter_guess variable that had previously been assign to '*'


import random
import requests
import bs4

TEXT_FILE_LOCATION = "english_words.txt"
with open(TEXT_FILE_LOCATION) as open_file:
    ENGLISH_WORDS = open_file.read().splitlines()

def pick_random_hidden_word(ENGLISH_WORDS):
    hidden_word = random.choice(ENGLISH_WORDS)
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


def get_letter_guess(letter_guess_record, hidden_word):
    letter_guess = input('Enter a letter to guess, or enter * for a clue >> \n').upper()
    print('letter guess = %s' % letter_guess)
    if letter_guess == '*':
        show_clue(hidden_word)
        letter_guess = get_letter_guess(letter_guess_record, hidden_word)
    elif letter_guess in letter_guess_record:
        print('You have already guessed %s. Please guess again!' % letter_guess)
        letter_guess = get_letter_guess(letter_guess_record, hidden_word)
    return letter_guess


def show_clue(hidden_word):
    url = 'http://www.wordreference.com/definition/' + hidden_word
    try:
        clue_page_request = requests.get(url)
        clue_page_request.raise_for_status()
        clue_page = bs4.BeautifulSoup(clue_page_request.text, "lxml")
        definition_tag = clue_page.select('span[class="rh_def"]')
        definition_text = definition_tag[0].get_text()
        print_clue_that_is_not_too_easy(definition_text)
    except:
        print('Unfortunately no clue is available. ' +
              'Perhaps your device is not connected to mankind\'s central nervous system.'
              '\nAlternatively there might not be a clue available for the word!\n')


def print_clue_that_is_not_too_easy(definition_text):
    separator_to_avoid_giving_a_clue_that_is_too_easy = ':'
    definition_text_without_an_easy_clue = definition_text.split(
        separator_to_avoid_giving_a_clue_that_is_too_easy, 1)[0]
    print('Okay! The clue is: \n%s\n' % definition_text_without_an_easy_clue)


def create_letter_guess_records():
    letter_guess_record = []
    number_of_guesses_record = 0 # create new function that records the number of incorrect guesses
    return (letter_guess_record, number_of_guesses_record)


def update_letter_guess_records(letter_guess, letter_guess_record, number_of_guesses_record):
    letter_guess_record.append(letter_guess)
    print('Letter guess record = {}'.format(str(letter_guess_record)))
    number_of_guesses_record = len(letter_guess_record)
    print('number of guesses record = {}'.format(str(number_of_guesses_record)))
    print_hangman_image_based_on_number_of_guesses(number_of_guesses_record) # Move this function outside of the update..function
    return (letter_guess_record, number_of_guesses_record)




str_image_16 = [
'''
 _ _ _ _  
 |     |   
 |   \ O / 
 |     |   
 |    / \  
_^_ _     
'''
]

str_image_15 = [
'''
 _ _ _ _  
 |     |   
 |   \ O / 
 |     |   
 |    /   
_^_ _     
'''
]

str_image_14 = [
'''
 _ _ _ _  
 |     |   
 |   \ O / 
 |     |   
 |       
_^_ _     
'''
]

str_image_13 = [
'''
 _ _ _ _  
 |     |   
 |   \ O / 
 |     |   
 |       
_^_ _     
'''
]

str_image_12 = [
'''
 _ _ _ _  
 |     |   
 |   \ O / 
 |        
 |       
_^_ _     
'''
]

str_image_11 = [
'''
 _ _ _ _  
 |     |   
 |   \ O  
 |        
 |       
_^_ _     
'''
]

str_image_10 = [
'''
 _ _ _ _  
 |     |   
 |     O  
 |        
 |       
_^_ _     
'''
]

str_image_9 = [
'''
 _ _ _ _  
 |     |   
 |       
 |        
 |       
_^_ _     
'''
]

str_image_8 = [
'''
 _ _ _ _  
 |        
 |       
 |        
 |       
_^_ _     
'''
]


str_images = [str_image_16, str_image_15, str_image_14, str_image_13, str_image_12,
              str_image_11, str_image_10, str_image_9, str_image_8]


def print_hangman_image_based_on_number_of_guesses(number_of_guesses):
    assert type(number_of_guesses) == int
    for line in str_images[number_of_guesses]:
        print(line)


def check_letter_guess_and_update(letter_guess, hidden_letter_and_marker_list):
    if len(letter_guess) == 1: # Note if letter_guess is longer than one character, letter_guess will be a word_guess
        correct_or_incorrect_guess_counter = 0
        for letter_and_marker_pair in hidden_letter_and_marker_list:
            for k in letter_and_marker_pair.keys():
                if k == letter_guess:
                    letter_and_marker_pair[k] = 1
                    correct_or_incorrect_guess_counter += 1
        return correct_or_incorrect_guess_counter


def print_message_and_get_value_of_true_if_the_most_recent_guess_is_correct(correct_or_incorrect_guess_counter, letter_guess):
    if correct_or_incorrect_guess_counter > 0:
        print('Correct! The letter %s appears in the word' % letter_guess)
        is_most_recent_guess_correct = True
        return is_the_most_recent_guess_correct
    else:
        print('Incorrect! The letter %s does not appear in the word' % letter_guess)
        is_most_recent_guess_correct = False
        return is_the_most_recent_guess_correct


def get_value_of_true_if_the_most_recent_guess_is_correct(correct_or_incorrect_guess_counter):
    if correct_or_incorrect_guess_counter > 0:
        is_the_most_recent_guess_correct = True
        return is_the_most_recent_guess_correct
    else:
        is_the_most_recent_guess_correct = False
        return is_the_most_recent_guess_correct


def check_whether_game_complete(hidden_letter_and_marker_list, hidden_word_length, letter_guess, hidden_word):
    if len(letter_guess) <= 1:
        is_game_finished = check_if_game_complete_based_on_letter_guess(hidden_letter_and_marker_list,
                                                                        hidden_word_length)
    elif len(letter_guess) > 1:
        word_guess = letter_guess
        is_game_finished = check_if_game_complete_based_on_word_guess(word_guess, hidden_word)
    return is_game_finished


def check_if_game_complete_based_on_letter_guess(hidden_letter_and_marker_list, hidden_word_length):
    number_of_correct_guesses = get_the_number_of_correctly_guessed_letters(hidden_letter_and_marker_list)
    if number_of_correct_guesses == hidden_word_length:
        is_game_finished = True
    else:
        is_game_finished = False
    return is_game_finished


def get_the_number_of_correctly_guessed_letters(hidden_letter_and_marker_list):
    game_progress_counter = 0
    for letter_and_marker_pair in hidden_letter_and_marker_list:
        for v in letter_and_marker_pair.values():
            if v is 1:
                game_progress_counter += 1
    return game_progress_counter


def check_if_game_complete_based_on_word_guess(word_guess, hidden_word):
    if word_guess == hidden_word:
        is_game_finished = True
    else:
        is_game_finished = False
    return is_game_finished


def show_end_of_game_congratulations(hidden_word):
    print('\nCongratulations! You guessed the hidden word \'%s\'!' % hidden_word.title())


def main_game_loop(is_game_finished, hidden_letter_and_marker_list,
                   hidden_word_length, hidden_word, letter_guess_record, number_of_guesses_record):
    while is_game_finished != True:
        letter_guess = get_letter_guess(letter_guess_record, hidden_word)
        if letter_guess == None:
            continue
        update_letter_guess_records(letter_guess, letter_guess_record, number_of_guesses_record)
        correct_or_incorrect_guess_counter = check_letter_guess_and_update(letter_guess, hidden_letter_and_marker_list)
        is_the_most_recent_guess_correct = print_message_and_get_value_of_true_if_the_most_recent_guess_is_correct(
            correct_or_incorrect_guess_counter, letter_guess)
        print_hidden_letter_and_marker_list(hidden_letter_and_marker_list)
        is_game_finished = check_whether_game_complete(hidden_letter_and_marker_list, hidden_word_length,
                                                       letter_guess, hidden_word)


def play_hangman_game():
    hidden_word = pick_random_hidden_word(ENGLISH_WORDS)
    #print(hidden_word)  # DBUG To remove
    hidden_word_length = get_hidden_word_length(hidden_word)
    hidden_letter_and_marker_list = generate_hidden_letters_and_markers_for(hidden_word)
    is_game_finished = False
    letter_guess_record, number_of_guesses_record = create_letter_guess_records()
    main_game_loop(is_game_finished, hidden_letter_and_marker_list,
                   hidden_word_length, hidden_word, letter_guess_record, number_of_guesses_record)
    show_end_of_game_congratulations(hidden_word)


# Engine

play_hangman_game()


