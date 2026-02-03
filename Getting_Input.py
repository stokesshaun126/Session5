name = input("What is your name?")
print("Nice to meet you",name)
# It runs but then you're expected to write your input to the question which it then yields back an answer

age = input("What is your age?")
try:
    age = int(age) # without putting int(age), python reads your input of age as a string "20"
    print("You were born in", 2025 - age)
except ValueError:
    print("that is not a proper age/number")
    print("don't be smart with me")
except NameError:
    print("you are misspelling something")
except:
    print("this will catch all other exceptions")
else:
    print("thanks for playing fair") # only if no exception is thrown
finally:
    print("this wil be done no matter what") # prints no matter if there are exceptions or not
