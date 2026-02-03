num = 1
while num <= 100:
    print(num)
    num = num + 1

# infinite loop with escape mechanism

num = 1
while True:
    print(num)
    num = num + 1
    if num > 100:
        break # break is the escape from the loop
         