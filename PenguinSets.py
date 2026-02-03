# IMPORTS
import csv
with open('C:/Users/aaron/PycharmProjects/CSDS237/Penguins_Data.csv') as f:
    penguins =[{k: v for k, v in row.items()} for row in csv.DictReader(f)]

# male_penguin_species = penguins["MALE"]
# female_penguin_species = penguins["FEMALE"]
