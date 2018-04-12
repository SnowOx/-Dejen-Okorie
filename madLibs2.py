#! python3
# MadLibs2.py - Programs that reads in text files and lets the user add their own text
# Could alter this program to create a method that separates each character (rather than each word as .split() does) in any string

#filename = input('Please enter the filename, with its extension, \nfor the program to read: ')
filename = 'madLibsInput.txt'  # For testing
openFile = open(filename, 'r')
readFile = openFile.read()
print('\nThe current file contains the text:\n\n ' + readFile + '\n')

# New File
writeFile = open('madLibsNewDocument%s.txt', 'w')

# Full Stop Separator -- iterate over the first split text and separate strings that have a '.' or ',' as the last character
splitText1 = readFile.split()
punctuation_list = ['.'] 
splitText2 = []
for word in splitText1:
    print(word)
    if word[-1] not in punctuation_list:
        splitText2.append(word)
    elif word[-1] in punctuation_list:
        splitText2.append(word[:-1])
        splitText2.append(word[-1])

print(splitText2)
# Word Replacer -- iterate over the list of separated words and punctutation and ask for input where element appears
elementsList = ['ADVERB','VERB','NOUN','ADJECTIVE']

for i in range(len(splitText2)):
    for element in elementsList:
        if element in splitText2[i]:
            newWord = input('The program found one ' + str(element) + '. What string would you like to replace it with? ')
            for character in punctuation_list:  # Add punctuation mark if punctation mark is present at the end of string
                if splitText2[i+1] == character:
                    splitText2[i] = str(newWord + splitText2[i+1] ) # If proceeding string is punctuation, join processing string
                    print(splitText2[i])        
                elif splitText2[i+1] != character:
                    splitText2[i] = str(newWord)            # Overwrite present word in list
                    print(splitText2[i])
        else:
            pass
        
# Floating Punctuation Remover -- remove the floating punctuation in the splitText2 list
for item in punctuation_list:
    for entry in splitText2:
        try:
            splitText2.remove(item)
            print('Deleted this floating punction mark >> ' + item)
        except:
            pass
        
# Join the refined string items
print(' '.join(splitText2))
writeFile.write(' '.join(splitText2))
writeFile.close()   
    
# Success! However, the code seems verbose.
