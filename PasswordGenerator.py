# IMPORTS
import string
import random

#Generate a random password with letters and digits of a given length
_passwordLength = input("Enter the password length: ")
_pwd = ""
while len(_pwd) < int(_passwordLength): _pwd += random.choice(string.ascii_letters + string.digits)
print("The password of length " + _passwordLength + " is " + _pwd + ".")
