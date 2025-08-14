import time
import os
import pyfiglet

def calc(num):  
    for multiplication in range(1, 11): # this serves as function for the increasing multiplyer up to 10
        result = num * multiplication  # the main logic for computing
        last = f"{num} X {multiplication} = {result}"  # this is for making a variable that the lenght syntax to read
        line = len(last)    # lenght syntax will read how many objects are will be printed
        time.sleep(1)    # added delay so it will be showed individually 

        print("╔" + "═" * line + "╗") # the "═" will be multiplied to the read lenght that will adapt to any number lenght
        print(f"║{last}║")   
        print("╚" + "═" * line + "╝")         

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')  

ascii_art = pyfiglet.figlet_format("MULTIPLICATION TABLES")
print(ascii_art)
print("Type a number you want to learn its multiplication table!!")

while True:
    print()
    print("===================================")
    num = int(input("Please input a number: "))
    print("===================================")
    calc(num)
    time.sleep(5)

    choice = input("would You like to try again? (Y/N): ") # it will ask the user if they want another table
    
   
    if choice == "N":
        print("Thank you for using!")       
        break

    clear_screen()  # this will run after they want to continue
                    
