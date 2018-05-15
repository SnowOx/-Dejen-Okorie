from random import randint
from time import sleep

MAX_NUMBER = 10

lower_bound = 1
upper_bound = MAX_NUMBER
chosen_number = -1

def set_chosen_number():
    global chosen_number
    chosen_number = randint(1, MAX_NUMBER)

def respond_to_guess(guess):
    global upper_bound
    global lower_bound
    if guess == chosen_number:
        return 0
    if guess > chosen_number:
        if guess <= upper_bound:
            upper_bound = guess - 1
        return -1
    # Guess must be < chosen_number
    if guess >= lower_bound:
        lower_bound = guess + 1
    return 1

def computer_guess(upper_bound,lower_bound):
    if upper_bound == lower_bound:
        return upper_bound
    return (upper_bound + lower_bound) // 2
    
def computers_turn():
    name = 'Computer'
    guess = computer_guess()
    thinking_time = randint(2, 5)
    print(f'{name} is thinking about the next guess...\n')
    #sleep(thinking_time)
    return players_turn(guess, name)

def humans_turn():
    guess = input('Try guessing the hidden number! -> ')
    try:
        return players_turn(int(guess), 'Player')
    except ValueError:
        print('That ain\'t a proper number. Do it again.\n')
        return humans_turn()

def players_turn(guess, player_name):
    print(f'{player_name} guesses * {guess} * ...\n')
    result = respond_to_guess(guess)
    if result == 0:
        print(f'{player_name} correctly guessed {guess}! {player_name} wins!\n')
        return True
    if result == 1:
        comparison = 'HIGHER' 
    else:
        comparison = 'LOWER'
    sleep(1)
    print(f'The guess is wrong... the hidden number is {comparison} than {guess}\n')
    return False

def play_the_game():
    set_chosen_number()
    humans_go = True
    game_over = False
    while not game_over:
        sleep(1)
        if humans_go:
            game_over = humans_turn()
        else:
            game_over = computers_turn()
            humans_go = not humans_go
            
play_the_game()

