i = 0
while i < 10:
    print(i)
    i = i + 1

print()
for i in range (10): # the whole thing is with range
    print(i)

# for does the initial step of i = 0 and the iterative step of i = i +1 for us. It starts the progression at 0 and then iterates
# while requires the specific inputs for the iteration

for i in range(0, 100, 7): #start, end, increment
    print(i)
# if you dont add a start or an increment, for implicitly puts the start as 0 and the increment as 1

for i in range(15):
    print(7*i)
for i in range(1, 11):
    for j in range (1, 11):
        print(f"{i} x {j} = {i*j}") # string: the f" prints the values of the objects in {} rather than verbatim
        print()

for i in range(1, 11):
    for j in range (i, 11): # this can use variables
        print(f"{i} x {j} = {i*j}")
        print()

