#! python3
# MadLibs2.py - Programs that reads in text files and lets the user add their own text


#filename = input('Please enter the filename with its extension: ')
filename = 'madLibsInput.txt' # For testing
openFile = open(filename, 'r')
readFile = openFile.read()
print('The current file contains the text:\n ' + readFile + '\n\n')
writeFile = open('aNewDocument.txt', 'w')

splitText1 = readFile.split()

# Full Stop Separator -- iterate over the first split text and separate strings that have a '.' or ',' as the last character
splitText2 = []
punctuation_list = ['.', ',']

##for word in splitText1:
##    print(word)
##    if word[-1] not in punctuation:
##        splitText2.append(word)
##        print(splitText2)
##    elif word[-1] in punctuation:
##        splitText2.append(word[:-1])
##        punctuationAndSpace = str(word[-1] + ' ') # Add space after each '.'
##        splitText2.append(punctuationAndSpace)
##        print(splitText2)

# Word Replacer -- iterate over the list of separated words and punctutation and ask for input where element appears
elementsList = ['ADVERB','VERB','NOUN','ADJECTIVE']
for i in range(len(splitText2)):
    for element in elementsList:
        if element in splitText2[i]:
            print(element)
            newWord = input('The program found one ' + str(element) + '. What string would you like to replace it with? ')
            for character in punctuation_list:  # Add punctuation mark if punctation mark is present at the end of string
                if splitText2[i[-1]] == character:
                    splitText2[i] = str(newWord + character)
                    print(splitText2[i])
                elif splitText2[i[-1]] != character:
                    splitText2[i] = str(newWord)
                    print(splitText2[i])
                    

                
        else:
            pass

# Punctuation-Sensitive Joiner -- Join text with ' ' unless there is punctuation        
##for segment in splitText2:
##    if segment not in punctuation:
##    (' '.join(splitText2))



writeFile.write(' '.join(splitText2))
writeFile.close()   
    
# Incomplete. Program currently overwrites full stops that are adjacent to the detected elements 
