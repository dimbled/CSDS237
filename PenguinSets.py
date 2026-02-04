# IMPORTS
from pprint import pprint
from collections import Counter
from collections import defaultdict

# Part 2: Sequences, Sets, and Mapping objects (continued)
# 4. Sets

# Use the following code snippet to create a list penguins from the given data file Penguins_Data.csv
# the provided code is below
import csv
with open('Penguins_Data.csv') as f:
    penguins =[{k: v for k, v in row.items()} for row in csv.DictReader(f)]

# Create sets male_penguin_species and female_penguin_species using the penguins list (of dictionaries)
# based on the gender of the penguin.
male_penguin_species = set() # initialize male penguin species set
female_penguin_species = set() # initialize female penguin species set
for dict in penguins:
    if dict["Gender"] == "MALE":
        male_penguin_species.add(dict["Species"])
    else:
        female_penguin_species.add(dict["Species"])

# Explore the species with male subjects but didn't have female subjects.
male_only_species = male_penguin_species.difference(female_penguin_species)
# the hint doesn't make sense, as it gives only the species with female subjects and without male subjects
# Also, female_penguin_species contains all the elements of male_penguin_species
print(f"The species with male subjects without female subjects are {male_only_species}"
      f" with length {len(male_only_species)}.")
# with the given Penguins_Data.csv, this will always yield the empty set
# there are no species containing only male penguins, so I'm not sure exactly what is expected here

# Find all the species in both sets and store the results as all_species.
all_species = female_penguin_species.union(male_penguin_species)
# this is the same as female_penguin_species for the reasons stated above
print(f"The species in the male and female sets are {all_species} with length {len(all_species)}.")

# Find all the species that occur in both sets.
species_with_male_female = female_penguin_species.intersection(male_penguin_species)
# this will yield male_penguin_species for the reasons stated above
print(f"The species with both male and female subjects are {species_with_male_female}"
      f" with length {len(species_with_male_female)}.")


# PART 3: Collections Module
# 1. Counter

# Create a Counter of the penguins list called penguin_gender_counts.
penguin_gender_counts = Counter(p["Gender"] for p in penguins)
print(penguin_gender_counts)

# Print the three most common species counts.
penguin_species_counts = Counter(p["Species"] for p in penguins)
print(penguin_species_counts)


#2. DefaultDict

# Create a defaultdict male_penguin_weights with list data type.
male_penguin_weights = defaultdict(list)

# Create a list male_penguins from penguins.
male_penguins = [p for p in penguins if p["Gender"] == "MALE"]

# Iterate over the male_penguins list, use species as the key of the male_penguin_weights dictionary and
# append the body_mass of each male penguin to its value.
for p in male_penguins:
    male_penguin_weights[p["Species"]].append(p["Body_Mass_g"])

# Use the .items() method to print the items of the male_penguin_weights dictionary.
pprint(male_penguin_weights.items())