import string

# Read a string and interpret it as an array of machine values
_str = input("Enter the string to be interpreted: ")
list = list(bytearray(_str, 'ascii'))
print(list)
