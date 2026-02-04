#IMPORTS
import re

# Find sequences of lowercase letters joined by an underscore.
_str = 'WEATher_is_14deg_less_than_NORMAL65' # initialize
str_list = re.findall("[a-z_]+", _str) # make list of series of lower alphas and underscores of any length
print(str_list)