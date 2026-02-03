# if + else
import random

num = random.randint(1,10)
print("random number is", num)

# check for odd
if not num % 2:
    print("number", num, "is even")
else: # like the opposite of the first if
    print("number", num, "is odd") # can only apply else when the second option is obvious because the first is false
    print("this only shows for odd numbers")
print("this shows always: thanks for playing")

