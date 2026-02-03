# simplest if
import random

num = random.randint(1,10)
print("random number is", num)

# check for odd
if num % 2 == 1: # == 1 is not needed, as the only 2 options are 0 and 1, which are True or False
    print("number", num, "is odd")

if num % 2 == 0: # this can be optimized and written as "if not num % 2"
        print("number", num, "is even")
