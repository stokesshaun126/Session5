# start with the most restrictive ask first, because once one condition is hit, the others are ignored even if satisfied
# order matters

money = 2000000

if money > 10**9:
    print("Welcome to Forbes List!")
elif money > 10**8:
    print("Welcome to Forbes up and coming!")
elif money > 10**7:
    print("Do you like your Ferraris")
elif money > 10**6:
    print("Millionaire, pretty good")
elif money > 10**5:
    print("Six figure worth, decent")
elif money > 10**4:
    print("Technically not poor")
else:
    print("I'm sorry")
