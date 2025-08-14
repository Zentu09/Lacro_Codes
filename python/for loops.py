import time

password = "ART"

for attempt in range(3):
    guess = input("please input your password: ")
    if guess == password:
        print("You may enter")
        time.sleep(1)
        print("\033[F\033[K")
        break
    else:
        print(f"Wrong password. You have {2 - attempt} attempts left")
        time.sleep(1)
        print()
else:
    print("You've guessed to many times now deleting OS")