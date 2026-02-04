# IMPORTS
import string

# Read a string and interpret it as an array of machine values
_str = input("Enter the string to be interpreted: ")
machine_list = list(bytearray(_str, 'ascii')) # interpret the string via a bytearray in ASCII
print(f"The string {_str} is interpreted as {str(machine_list)} in ASCII.")