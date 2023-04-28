from random import random
num = random() * 100

num = int(num)
count = 1
guess_num = int(input("Guess the a number (1-100) : "))
while guess_num != num:
    if guess_num < num:
        print("Try a Higher Value!")
    else:
        print("Try a Lower Value!")
    guess_num = int(input("Guess the winning number : "))
    count += 1
else:
    print(f"You Won!!! {guess_num} is the winning number !")
    if count > 1:
        print(f"You took {count} attempts.")
    else:
        print(f"You did it in the {count}st attempt.")