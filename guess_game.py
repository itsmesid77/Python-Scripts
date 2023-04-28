from random import random, randrange

# num = int(random() * 100)
num = randrange(1,100)
chances = 1
guess_num = int(input("Enter a random number (1-100): "))
while guess_num != num:
    if guess_num < num:
        print("Higher")
    elif guess_num > num:
        print("lower")
    guess_num = int(input("Try Again (1-100): "))
    chances += 1
else:
    print("Congratulation! You guessed the right number which is",num)
    if chances == 1:
        print("You did it in the first attempt.")
    else:
        print(f"You took {chances} attempts.")

   