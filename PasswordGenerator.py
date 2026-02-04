# IMPORTS
import string
import random

#Generate a random password with letters and digits of a given length
_passwordLength = input("Enter the password length: ")
_pwd = "" # initialize pwd to return
while len(_pwd) < int(_passwordLength): # repeat until the desired length is reached
    _pwd += random.choice(string.ascii_letters + string.digits) # append a random alphanumerical character
print("The password of length " + _passwordLength + " is " + _pwd + ".")
