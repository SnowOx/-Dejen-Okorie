#! python3
# madlibs.py

import sys
import time

# Open and read file
text = open(sys.argv[1], 'r')
contents = text.read()
print('The specified file contains the text: \n' + contents)

# User input
newAdjective = input('Please enter an adjective >> ')
newNoun = input('Please enter a noun >> ')
newAdverb = input('Please enter a adverb >> ')
newVerb = input('Please enter a verb >> ')

# Replace ADJECTIVE, NOUN, ADVERB, or VERB in text



# Save new file with the newly created text
print('Saving new MadLibs file ...')
dateString = str(time.strftime("%H%M%S-%d%m%y"))
newFile = open(f'MadLib{dateString}.txt', 'r')
newContents = newFile.read()
for line in newContents:
    contents.replace('ADJECTIVE', newAdjective)
    contents.replace('NOUN', newNoun)
    contents.replace('ADVERB', newAdverb)
    contents.replace('VERB', newVerb)

newFile.write(newContents)
newFile.close()
newContents = open(f'MadLib{dateString}.txt', 'r')

print(f'The MadLibs file {dateString} was created and contains: \n' + readNewContents)
newContents.close()


