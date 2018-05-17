#! python3
# palindrome_checker.py
input_str = 'rat tar'

def check_if_str_is_a_palindrome(input_str):
    letters_list = input_str.replace(' ', '').split()
    for i in range(len(letters_list)):
  	if letters_list[i] != letters_list[-i]:
        print('%s is not a palindrome' % input_str)
  		return False
    print('%s is a palindrome' % input_str)
    return True
  
check_if_str_is_a_palindrome(input_str)
