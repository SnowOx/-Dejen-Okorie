#! python3
# hangman_game.py

# Begin by creating a hangman game for a human guesser -> Completed
# # Would like to create a GUI after I have completed the basic mechanics


import random
import requests
import bs4

TEXT_FILE_LOCATION = "english_words.txt"
with open(TEXT_FILE_LOCATION) as open_file:
    ENGLISH_WORDS = open_file.read().splitlines()

str_image_11 = [
    '''
     _ _ _ _  
     |     |   
     |   \ O / 
     |     |                   Game over!
     |    / \  
    _^_ _     
    '''
]

str_image_10 = [
    '''
     _ _ _ _  
     |     |   
     |   \ O / 
     |     |                   You have one life remaining!
     |    / \  
    _^_ _     
    '''
]

str_image_9 = [
    '''
     _ _ _ _  
     |     |   
     |   \ O /              
     |     |                    You have two lives remaining!
     |    /  
    _^_ _     
    '''
]

str_image_8 = [
    '''
     _ _ _ _  
     |     |   
     |   \ O / 
     |     |   
     |       
    _^_ _     
    '''
]

str_image_7 = [
    '''
     _ _ _ _  
     |     |   
     |   \ O / 
     |        
     |       
    _^_ _     
    '''
]

str_image_6 = [
    '''
     _ _ _ _  
     |     |   
     |   \ O  
     |        
     |       
    _^_ _     
    '''
]

str_image_5 = [
    '''
     _ _ _ _  
     |     |   
     |     O  
     |        
     |       
    _^_ _     
    '''
]

str_image_4 = [
    '''
     _ _ _ _  
     |     |   
     |       
     |        
     |       
    _^_ _     
    '''
]

str_image_3 = [
    '''
     _ _ _ _  
     |        
     |       
     |        
     |       
    _^_ _     
    '''
]

str_image_2 = [
    '''
    
     |        
     |       
     |        
     |       
    _^_ _     
    '''
]

str_image_1 = [
    '''
    
    
    
    
    
    _ _ _     
    '''
]

str_images = [str_image_1, str_image_2, str_image_3, str_image_4, str_image_5, str_image_6, str_image_7,str_image_8,
              str_image_9, str_image_10, str_image_11]


NUMBER_OF_PERMITTED_GUESSES = len(str_images)


def pick_random_hidden_word():
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


def get_guess(guess_record, hidden_word):
    guess = input('\nEnter a letter to guess, or enter * for a clue >> \n').upper()
    if guess == '*':
        show_clue(hidden_word)
        guess = get_guess(guess_record, hidden_word)
    elif guess in guess_record:
        print('You have already guessed %s. Please guess again!' % guess)
        guess = get_guess(guess_record, hidden_word)
    elif not guess.isalpha():
        print('Your guess was invalid. Please enter another guess!')
        guess = get_guess(guess_record, hidden_word)
    return guess


def show_clue(hidden_word):
    url = 'http://www.wordreference.com/definition/' + hidden_word
    try:
        clue_page_request = requests.get(url)
        clue_page_request.raise_for_status()
        clue_page = bs4.BeautifulSoup(clue_page_request.text, "lxml")
        definition_tag = clue_page.select('span[class="rh_def"]')
        definition_text = definition_tag[0].get_text()
        print_clue_that_is_not_too_easy(definition_text)
    except: # Change this to a specific exception
        print('Unfortunately no clue is available. ' +
              'Perhaps your device is not connected to mankind\'s central nervous system.'
              '\nAlternatively there might not be a clue available for the word!\n')


def print_clue_that_is_not_too_easy(definition_text):
    separator_to_avoid_giving_a_clue_that_is_too_easy = ':'  # OPerhaps alter this to improve the clue's presentation
    definition_text_without_an_easy_clue = definition_text.split(
        separator_to_avoid_giving_a_clue_that_is_too_easy, 1)[0]
    print('Okay! The clue is: \n%s' % definition_text_without_an_easy_clue)


def create_guess_record():
    guess_record = []
    return guess_record


def update_guess_records(guess, guess_record):
    guess_record.append(guess)
    print('So far, the letters and words that you have guessed include {}'.format(', '.join(guess_record)))
    return guess_record


def check_letter_guess_and_update(guess, hidden_letter_and_marker_list):
    correct_guess_counter = 0  # Query: Replace this binary counter with Boolean?
    for letter_and_marker_pair in hidden_letter_and_marker_list:
        for k in letter_and_marker_pair.keys():
            if k == guess:
                letter_and_marker_pair[k] = 1
                correct_guess_counter += 1
    return correct_guess_counter


def print_correct_or_incorrect_message(correct_guess_counter, guess):
    if len(guess) == 1:
        if correct_guess_counter > 0:
            print('Correct guess! The letter \'%s\' appears in the hidden word' % guess)
        else:
            print('Incorrect! \'%s\' does not appear in the hidden word' % guess)
    if len(guess) > 1 and correct_guess_counter == 0:
            print('Incorrect! The hidden word is not \'%s\'' % guess.title())


def create_record_of_number_of_incorrect_guesses():
    record_of_number_of_incorrect_guesses = 0
    return record_of_number_of_incorrect_guesses


def add_incorrect_guesses_to_the_record_of_incorrect_guesses(correct_guess_counter,
                                                             record_of_number_of_incorrect_guesses):
    if correct_guess_counter == 0:
        record_of_number_of_incorrect_guesses += 1
    elif correct_guess_counter == 1:
        record_of_number_of_incorrect_guesses += 0
    return record_of_number_of_incorrect_guesses


def print_hangman_image_based_on_number_of_incorrect_guesses(record_of_number_of_incorrect_guesses,
                                                             correct_guess_counter):
    assert type(record_of_number_of_incorrect_guesses) == int
    if correct_guess_counter == 0:
        for line in str_images[record_of_number_of_incorrect_guesses - 1]:
            print(line)


def check_whether_game_complete_based_on_letter_guess(hidden_letter_and_marker_list, hidden_word_length):
    is_game_complete = check_if_game_complete_based_on_guess(hidden_letter_and_marker_list, hidden_word_length)
    return is_game_complete


def check_if_game_complete_based_on_guess(hidden_letter_and_marker_list, hidden_word_length):
    number_of_correct_guesses = get_the_number_of_correctly_guessed_letters(hidden_letter_and_marker_list)
    if number_of_correct_guesses == hidden_word_length:
        is_game_complete = True
    else:
        is_game_complete = False
    return is_game_complete


def get_the_number_of_correctly_guessed_letters(hidden_letter_and_marker_list):
    game_progress_counter = 0
    for letter_and_marker_pair in hidden_letter_and_marker_list:
        for v in letter_and_marker_pair.values():
            if v is 1:
                game_progress_counter += 1
    return game_progress_counter


def check_if_game_complete_based_on_word_guess(word_guess, hidden_word):
    if word_guess == hidden_word:
        is_game_complete = True
        correct_guess_counter = 1
    else:
        is_game_complete = False
        correct_guess_counter = 0
    return (is_game_complete, correct_guess_counter)


def check_whether_game_over_and_incomplete(record_of_number_of_incorrect_guesses):
    if record_of_number_of_incorrect_guesses >= NUMBER_OF_PERMITTED_GUESSES:
        is_game_over_and_incomplete = True
        return is_game_over_and_incomplete


def show_end_of_game_congratulations(hidden_word):
    print('\nCongratulations! You guessed the hidden word \'%s\'!' % hidden_word.title())


def show_end_of_game_comiserations(hidden_word):
    print("\nUnfortunately you failed to guess the hidden word before running out of lives. \n" +
          "The hidden word was '%s'!" % hidden_word.title())


def main_game_loop(is_game_complete, hidden_letter_and_marker_list, hidden_word_length, hidden_word,
                   guess_record, record_of_number_of_incorrect_guesses,
                   is_game_over_and_incomplete):
    while is_game_complete is not True and is_game_over_and_incomplete is not True:
        guess = get_guess(guess_record, hidden_word)
        update_guess_records(guess, guess_record)
        if len(guess) > 1:
            is_game_complete, correct_guess_counter = check_if_game_complete_based_on_word_guess(guess, hidden_word)
            if is_game_complete:
                return 'won game'
        elif len(guess) == 1:
            correct_guess_counter = check_letter_guess_and_update(guess, hidden_letter_and_marker_list)
            is_game_complete = check_whether_game_complete_based_on_letter_guess(hidden_letter_and_marker_list,
                                                                                 hidden_word_length)
        print_correct_or_incorrect_message(correct_guess_counter, guess)
        record_of_number_of_incorrect_guesses = add_incorrect_guesses_to_the_record_of_incorrect_guesses(
                                                        correct_guess_counter, record_of_number_of_incorrect_guesses)
        print_hangman_image_based_on_number_of_incorrect_guesses(record_of_number_of_incorrect_guesses,
                                                                 correct_guess_counter)
        print_hidden_letter_and_marker_list(hidden_letter_and_marker_list)
        if is_game_complete:
            return 'won game'
        is_game_over_and_incomplete = check_whether_game_over_and_incomplete(record_of_number_of_incorrect_guesses)
        if is_game_over_and_incomplete:
            return 'lost game'


def play_hangman_game():
    hidden_word = pick_random_hidden_word()
    hidden_word_length = get_hidden_word_length(hidden_word)
    hidden_letter_and_marker_list = generate_hidden_letters_and_markers_for(hidden_word)
    is_game_complete = False
    is_game_over_and_incomplete = False
    guess_record = create_guess_record()
    record_of_number_of_incorrect_guesses = create_record_of_number_of_incorrect_guesses()
    result = main_game_loop(is_game_complete, hidden_letter_and_marker_list, hidden_word_length, hidden_word,
                            guess_record, record_of_number_of_incorrect_guesses, is_game_over_and_incomplete)
    if result == 'won game':
        show_end_of_game_congratulations(hidden_word)
    if result == 'lost game':
        show_end_of_game_comiserations(hidden_word)


# Engine
play_hangman_game()
