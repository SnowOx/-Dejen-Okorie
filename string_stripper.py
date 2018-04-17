#! python3
# string_stripper.py

import re

def string_strip(input_string, *user_characters):
    if not user_characters:
        no_white_regex = re.compile(r'\w')
        stripped_string = no_white_regex.findall(input_string)
        output_string = ''.join(stripped_string)
        return output_string
    if user_characters:
        user_regex = re.compile(r'(%s)' % user_characters)
        stripped_string = user_regex.findall(input_string)
        print(stripped_string)
        output_string = ''.join(stripped_string)
        print(output_string)
        return output_string

string_strip('The cat hat cat 24332', 'at')
