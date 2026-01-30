#IMPORTS

# Find sequences of lowercase letters joined by an underscore.
# ASK FOR MORE SPECIFICITY

_str = 'WEATher_is_14deg_less_than_NORMAL65'

_fixedStr = "".join(filter(str.isalpha, _str))
