#IMPORTS
import math

# Calculate the distance btween the points (x1, y1) and (x2, y2)
_x1 = input("Enter the first x coordinate: ")
_y1 = input("Enter the first y coordinate: ")
_x2 = input("Enter the second x coordinate: ")
_y2 = input("Enter the second y coordinate: ")
_d = math.sqrt((float(_x2) - float(_x1)) ** 2 + (float(_y2) - float(_y1)) ** 2)
print("The distance between points (" + _x1 + "," + _y1 + ") and (" + _x2 + "," + _y2 + ") is " + str(_d) + ".")
