#! python3
# string_stripper.py

import re

def remove_whitespace(input_string):
    no_white_regex = re.compile(r'\w')
    stripped_string = no_white_regex.findall(input_string)
    output_string = ''.join(stripped_string)
    return output_string

def remove_user_defined_characters(input_string, user_characters):
    print(user_characters)
    user_regex = re.compile(rf'^((?!{user_characters[0]}).)*$')
    stripped_string = user_regex.findall(input_string)
    print(stripped_string)
    output_string = ''.join(stripped_string)
    return output_string
    
def string_strip(input_string, *user_characters):
    if not user_characters:
        return remove_whitespace(input_string)   
    return remove_user_defined_characters(input_string, user_characters)
        
print(string_strip('The tiki taka cat hat cat 24332', 'at'))
