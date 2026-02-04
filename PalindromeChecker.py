#IMPORTS

# Check if a given string is a palindrome
# NOTE: I ignore spaces and non-alphabet characters in order to accept longer palindromes
_str = input("Enter a string, and I will check if it is a palindrome: ")
# eliminate all nonalphanumeric characters and convert to lowercase
_fixedStr = "".join(filter(str.isalnum, _str)).lower()
_len = len(_fixedStr) # get the length of the formatted string
_halfLen = int(len(_fixedStr) / 2) # this is how many times we will check (only need to check half of the string)
isPalindrome = True # default to true

for i in range(_halfLen): # iterate through half the string from either direction
    if _fixedStr[i] != _fixedStr[_len - i - 1]: # check if the character at the index and "reverse index" are the same
        isPalindrome = False # if they don't match, it's not a palindrome
        break # break out of logic if a non-matching pair is found

if isPalindrome:
    print(f"{_str} is a palindrome.")
else:
    print(f"{_str} is not a palindrome.")