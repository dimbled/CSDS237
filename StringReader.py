import string

# Read a string and interpret it as an array of machine values
# WHAT IS THIS ASKING ??????
_str = input("Enter the string to be interpreted: ")
_list = list(_str)
print(_list)
_ba = bytearray(_str, 'ascii')
print(_ba)