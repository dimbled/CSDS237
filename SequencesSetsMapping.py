import os
import csv
from enum import unique
from itertools import zip_longest


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


# 2. Tuples QUESTION DO YOU WANT US TO REBUILD THE LISTS WITH THEIR RANKS INCLUDED?????

# Use the zip() function to pair up girl_names and boy_names into a variable called pairs.
pairs = zip_longest(girl_names, boy_names, fillvalue = "Name") # using zip longest to avoid losing names!

# Unpack each tuple pair of girl and boy name and their position.
unpacked_pairs = enumerate(pairs)

# Print the names in the following format. Rank #: Girlname and Boyname where the number # is the position of each pair.
for pair in unpacked_pairs:
     print(f"Rank #{pair[0]}: {pair[1][0]} and {pair[1][1]}")

# 3. Dictionaries

# Organize the baby names in a nested dictionary babynames_dict in the following format:
# the provided code is below
babynames_dict = current = {}
ethnicity = set([item[2] for item in records])
gender = set([item[1] for item in records])

from pprint import pprint
for e in ethnicity:
    current[e] = {}
    for g in gender:
        next_1 = {g : {}}
        current[e].update(next_1)
pprint(babynames_dict)

for item in records: # DO YOU WANT US TO INCLUDE YEAR?
    name = {int(item[0]): {item[3].capitalize() : (int(item[4]), int(item[5]))} } # added year to the provided code
    babynames_dict[item[2]][item[1]].update(name)
pprint(babynames_dict)

# Access babynames_dict and print the ethnicities in alphabetical order.
ethnicities = list(babynames_dict.keys())
ethnicities.sort()
print(ethnicities)


# Check if the key 'American Indian' is in the dictionary. Print 'Not found' if the key is not found in the dictionary.
print(babynames_dict.get("American Indian", "Not Found"))

# Update the dictionary with the key 'American Indian' with the given value. { "FEMALE": { "2017": {} } }.
babynames_dict.update({ "American Indian": {"FEMALE": { "2017": {} } } })
# I did "American Indian" instead of the more consistent "AMERICAN INDIAN"


# Remove the key 'Hispanic' from the dictionary.
# Save the result in babynames_hispanic.
babynames_hispanic = babynames_dict.pop("HISPANIC")
# I had to use "HISPANIC" and not the suggested "Hispanic"

# Generate a list of unique baby names in alphabetical order from babynames_hispanic dictionary.
# Print the number of baby names in the list.

unique_babynames_hispanic = []

# temp_list = []
#
# for items in babynames_hispanic.items():
#     for values in items:
#         temp_value = str(values)
#         # print(temp_value)
#         temp_list.append(temp_value.rsplit())
#
#         print(temp_list)
#

# pprint(unique_babynames_hispanic[3])
