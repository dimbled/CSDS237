#IMPORTS
import re
# Find sequences of lowercase letters joined by an underscore.

str = 'WEATher_is_14deg_less_than_NORMAL65' # initialize
str_list = re.findall("[a-z_]+", str) # make list of series of lower alphas and underscores of any length
print(str_list)
