# IMPORTS
import math
import random
import string

# Get the volume of a sphere with radius 6
_r = 6.0
_v = 4.0 / 3.0 * ( math.pi * _r ** 3)
print("The volume of a sphere with radius " + str(_r) + " is " + str(_v) + ".")

# Calculate the distance btween the points (x1, y1) and (x2, y2)
_x1 = input("Enter the first x coordinate: ")
_y1 = input("Enter the first y coordinate: ")
_x2 = input("Enter the second x coordinate: ")
_y2 = input("Enter the second y coordinate: ")
_d = math.sqrt((float(_x2) - float(_x1)) ** 2 + (float(_y2) - float(_y1)) ** 2)
print("The distance between points (" + _x1 + "," + _y1 + ") and (" + _x2 + "," + _y2 + ") is " + str(_d) + ".")

#Generate a random password with letters and digits of a given length
_passwordLength = input("Enter the password length: ")
_pwd = ""
while len(_pwd) < int(_passwordLength): _pwd += random.choice(string.ascii_letters + string.digits)
print("The password of length " + _passwordLength + " is " + _pwd + ".")