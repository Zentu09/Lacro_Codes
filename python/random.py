import random
import time

while True:
    rand_number = random.randint(1, 21)

    while True:
        lucky = rand_number
        guess = int(input("Guess the number!! (1-20): "))    
        
        if guess != lucky:  
            print(f"Wrong!! Try again")
            time.sleep(1)
            print()       
          
        else:
            print("You've guessed Right!!")
            time.sleep(1)
            print() 
            break

    playagain = input("Would you like to play again? (Y/N): ").strip().lower()
    print()

    if playagain == "N":
        print("Thank you for playing!!")

    elif playagain == "Y":
        break    
      

