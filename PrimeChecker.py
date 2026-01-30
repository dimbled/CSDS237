import math

_numberToCheck = input("Enter a number, and I'll check if it is prime: ")
_n = int(_numberToCheck)
_sqrt = int(math.sqrt(_n) + 1)
isPrime = True # default to true

if (_n <= 1): #check for 1 and negative numbers
    isPrime = False # 1 is not prime, but passes the standard logic
else: # most other inputs will go here
    for i in range(2, _sqrt): # standard logic
        if ((_n / i) % 1 == 0): # if a factor is found
            isPrime = False # update prime status
            break # and print

print(_numberToCheck + " is a prime number.") if isPrime else print(_numberToCheck + " is not a prime number.")


