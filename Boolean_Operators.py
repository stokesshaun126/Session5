# Boolean is logical operators - whether something is true or false (or, and, not)
True
False
# If the statement is or, once you match a statement you don't care what comes next. *Matching at least one
# If the statement is and, you care as the statements all have to apply. *Matching all
print(True and False)
print(True or False)
# False is considered 0, 0.0, False, None, "", etc
print(5 or 7) # it only prints 5 as we stop caring once we get a match
print(5 and 7) # it prints 7 (the last object) as it wants one that matches everything
print(None or False or 11 or 12 or 0) # it prints 11 as it is the first True match
print(None or False or 0 or "") # prints the empty string ""
print(7 and 8 and 0 and 9 and 10) # prints 0 as it is the first one that breaks the chain, the numbers after are True but 0 is false
print( 7 and 8 and 9 and 10)
# the or statement prints the first one that matches, and prints the first one to break the chain

# not - (the opposite of the object)
print("not 7 is ", not 7) # because 7 is true, not 7 is false
print("not 0 is", not 0)

