wining_number = 27
a = input("Guess  Number (1-100) : ")
a = int(a)
if a == wining_number:
    print("You Win!!!")
else:
    if a < wining_number:
        print("LOW!!!")
    else:
        print("High!!!")
