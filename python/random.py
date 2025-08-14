import random
import time

colors = ["RED", "YELLOW", "BLUE"]

while True:
    choice = random.choice(colors)
    guess = input("Guess a primary color!! (RED, BLUE & YELLOW): ").upper()

    if guess == choice:
        print("You've guessed Right!!")
        time.sleep(1)
        print()
    else:
        print(f"Wrong!! it was {choice}")
        time.sleep(1)
        print()
    playagain = input("Would you like to play again? (Y/N): ")
    print()
    
    if playagain == "N":
        print("Thank you for playing!!")

    while True:
        if playagain == "Y":
            continue
        else:
            print("wrong input")  
            break
        
    

