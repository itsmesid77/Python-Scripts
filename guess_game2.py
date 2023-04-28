import random 
winning_score_number = random.randint(1,100)
winning_number = 43
guess = 1
number = int(input("Enter a number(1-100): "))
game_over = False
while not game_over:
    if number == winning_number:
        print(f"You WIN! and guessed the number in {guess} times.")
        game_over = True
    else:
        if number < winning_number:
            print("Too Low!!")
            guess += 1
            number = int(input("Guess Again!!"))
        else:
            print("Too High!!")
            guess += 1
            number = int(input("Guess Again!!"))
        