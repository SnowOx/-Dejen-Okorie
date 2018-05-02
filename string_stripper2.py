#!python3
# strip_string.py

import re

def remove_whitespace(input_string):
    no_white_regex = re.compile(r'\w')
    stripped_string = no_white_regex.findall(input_string)
    output_string = ''.join(stripped_string)
    return output_string

def remove_user_defined_characters(input_string, user_characters):
    user_regex = re.compile('%s' % user_characters)
    stripped_string = user_regex.sub('', input_string)
    output_string = ''.join(stripped_string)
    return output_string

def strip_string(input_string, *user_characters):
    if not user_characters:
        return remove_whitespace(input_string)
    return remove_user_defined_characters(input_string, user_characters)

strip_string(input_string, *user_characters)

# Solved!
