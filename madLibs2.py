#! python3
# MadLibs2.py - Programs that reads in text files and lets the user add their own text


#filename = input('Please enter the filename with its extension: ')
filename = 'madLibsInput.txt' # For testing
openFile = open(filename, 'r')
readFile = openFile.read()
print('The current file contains the text:\n ' + readFile + '\n\n')
writeFile = open('aNewDocument.txt', 'w')

elementsList = ['ADVERB','VERB','NOUN','ADJECTIVE']
splitText = readFile.split()

print(splitText)

for i in range(len(splitText)):
    for element in elementsList:
        if element in splitText[i]:
            newWord = input('The program found one ' + str(element) + '. What string would you like to replace it with? ')
            splitText[i] = newWord
        else:
            pass
print(' '.join(splitText))
writeFile.write(' '.join(splitText))
writeFile.close()   
    
# Incomplete. Program currently overwrites full stops that are adjacent to the detected elements 
