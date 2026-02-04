# IMPORTS

# Find the length of the longest word in a sentence
_sent = input("Enter sentence: ") # get input
_splitSent = _sent.split() # split the input into words
_fixedSplitSent = _splitSent.copy() # create a copy to fix up
_longestLen = 0 # initialize longest word length at 0
_longestID = 0 # initialize id of longest word at 0

for i in range(len(_fixedSplitSent)): # iterate through each word in the array of words
    _fixedSplitSent[i] = "".join(filter(str.isalpha, _fixedSplitSent[i])) # fix each word by removing nonalpha chars
    if (len(_fixedSplitSent[i]) > _longestLen): # if the current word is the longest
        _longestLen = len(_fixedSplitSent[i]) # update the longest word length
        _longestID = i # update the position of the longest word for retrieval

print(f"The longest word in the sentence: {_sent} is {_splitSent[_longestID]}"
      f" with length of {str(_longestLen)} characters.")