#! python3
# cardGuessGame.py

# Note that I use f-strings below.

import random


# Generate the computer's hidden card
hiddenCard = random.randint(1, 52)

# Create dictionary and lists to serve as short term memory storage
previousGuessesDict = {}
gameWinner = [0]
gameStatus = [0]
guessChecker = [0]

# Human guessing functions, including higher and lower element
def humanTurn():
    humanGuess = int(input('Please enter your guess! \n'))

    if humanGuess == hiddenCard:
        print(f'CORRECT! You guessed the correct card, {hiddenCard}!')
        # Add exit element here ## Use return or dictionary?
        gameWinner[0] = 'You'
        gameStatus[0] = 'complete'

    else:
        if humanGuess > hiddenCard:
            print('Incorrect. The hidden card is lower than your guess')
            higherOrLowerIndication = 'lower'
            previousGuessesDict.update({humanGuess: higherOrLowerIndication})
        elif humanGuess < hiddenCard: # I realise that I could use an 'else' here to lower the amount of code. However, the current approach seems more readable
            print('Incorrect. The hidden card is higher than your guess')
            higherOrLowerIndication = 'higher'
            previousGuessesDict.update({humanGuess: higherOrLowerIndication})
        
# Computer guessing functions, including higher and lower element
def computerMemoryChecker(computerGuess):
    countAll = 0
    checkAll = 0
        
    if previousGuessesDict == True:             # Empty dictionary returns False
        for k, v in previousGuessesDict.items():
            countAll += 1                       # Counts each key value pair in the dictionary
            if (v == 'higher' and computerGuess > k or v == 'lower' and computerGuess < k):
                checkAll += 1
            else:
                pass                        # Does not add 1 if the checkingCounter check is unsucessful. computerTurn() should then re-loop and guess a new number
        print('checkAll = ' + checkAll)
        if countAll == checkAll:
            guessChecker[0] = 'success'
        elif countAll != checkAll:
            guessChecker[0] = 'failure' 
                        
    elif previousGuessesDict != True:          # Empty dictionary returns False
        pass

def computerTurn():
    while True:
        computerGuess = random.randint(1,52)
        computerMemoryChecker(computerGuess)

        if guessChecker[0] != 'success':                  ####! Tricky section here. The computer is stuck on these four lines
            continue
        else:
            pass
        
        if previousGuessesDict == True:
            if computerGuess in previousGuessesDict.values() == True:
                continue
            elif computerGuess in previousGuessesDict.values() == False:
                pass
        else:
            break

    print(f'The computer guessed {computerGuess}!')
    
    if computerGuess == hiddenCard:             # Check new guess against the hidden card
        print(f'CORRECT! The computer guessed the correct card, {hiddenCard}!')
    # Exit elements below
        gameWinner[0] = 'The computer'
        gameStatus[0] = 'complete'

    else:
        if computerGuess > hiddenCard:
            print('The computer\'s guess was incorrect. \nThe hidden card is lower than the computer\'s guess')
            higherOrLowerIndication = 'lower'

        elif computerGuess < hiddenCard:
            print('The computer\'s guess was incorrect. \nThe hidden card is higher than the computer\'s guess')
            higherOrLowerIndication = 'higher'
            
        previousGuessesDict.update({computerGuess: higherOrLowerIndication})  # Update previousGuessesDict with computer's guess and higherOrLowerIndication
    

# Game engine. The below involves checking if the game is complete before each guess
humanGuessFirst = input(
'This game involves competing against a computer to see \
who can guess a randomly chosen number first.\
\n\nAfter each guess, the player will be told if the randomly \
chosen number is higher or lower than the hidden number.\
\n\nWould you like to guess first? Enter yes or no: '
                        )

if humanGuessFirst.lower() == 'yes':
    print('You will guess first')
    while gameStatus == [] or gameStatus[0] != 'complete':
        humanTurn()
        print(previousGuessesDict, gameWinner, gameStatus) # Bug hunter
        if gameStatus[0] != 'complete':
            computerTurn()
            print(previousGuessesDict, gameWinner, gameStatus) # Bug hunter
        else:
            break

elif humanGuessFirst.lower() != 'yes':
    print('The computer will guess first')
    while gameStatus == [] or gameStatus[0] != 'complete':
        computerTurn()
        print(previousGuessesDict, gameWinner, gameStatus) # Bug hunter
        if gameStatus[0] != 'complete':
            humanTurn()
            print(previousGuessesDict, gameWinner, gameStatus) # Bug hunter
        else:
            break

print(f'Game complete. {gameWinner[0]} won the game!')
print(previousGuessesDict, gameWinner, gameStatus) # Bug hunter





