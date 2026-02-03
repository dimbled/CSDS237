import os
import csv

# 1. Lists

# below is the provided code
def csv_to_array(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        return list(reader)

records = csv_to_array('C:/Users/aaron/PycharmProjects/CSDS237/Popular_Baby_Names.csv')

# Create a list called baby_names that contain the name found in the fourth element in records.
# Capitalize and sort the list in alphabetical order.
baby_names = [record[3].capitalize() for record in records] # assembles list of names and capitalizes them
baby_names.sort() # sorts list of names


# Find the list of unique baby_names using set() function, and print the number of unique baby names in the list.
names_set = set(baby_names) # creates a set from the list of names
print(len(names_set)) # prints number of items in the set of unique baby names

# Use the .extend() method on baby_names_sorted to add 'Ida', 'Will', 'Sandeep', 'Jim', 'Karthik'. Sort the list.
baby_names_sorted = list(names_set) # create a list from the set to eliminate duplicates
names_to_add = ['Ida', 'Will', 'Sandeep', 'Jim', 'Karthik'] # initialize new names into new name list
baby_names_sorted.extend(names_to_add) # add new names to list of sorted names
baby_names_sorted.sort() # sort the list

# Remove names starting with 'X' from the list
baby_names_without_x = [] # initialize new list
for name in baby_names_sorted: # iterate through sorted list of names
    if not name.startswith('X'): # if the name does NOT start with X
        baby_names_without_x.append(name) # add it to the new list

# Create a list of boy_names and girl_names. Print the girl_names that start with 'S'.
boy_names = [] # initialize boy names list
girl_names = [] # initialize girl names list
for record in records: # fill both lists simultaneously
    if record[1] == 'FEMALE':
        girl_names.append(record[3])
    else:
        boy_names.append(record[3])

# sort the list of girl names as we did for the names above
girl_names = [names.capitalize() for names in girl_names]
girl_names = list(set(girl_names))
girl_names.sort()

# let's do the same for the boy names...
boy_names = [names.capitalize() for names in boy_names]
boy_names = list(set(boy_names))
boy_names.sort()

for name in girl_names: # iterate through each girl name
    if name.startswith('S'): # if the name starts with S
        print(name) # print it!

# 2. Tuples

# Use the zip() function to pair up girl_names and boy_names into a variable called pairs.
pairs = zip(boy_names, girl_names)

# Unpack each tuple pair of girl and boy name and their position.


