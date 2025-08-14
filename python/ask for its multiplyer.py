import time
import os
import pyfiglet

def calc(num):  
    for multiplication in range(1, 11):
        result = num * multiplication
        last = f"{num} X {multiplication} = {result}"    
        line = len(last)    
        time.sleep(1)    


        print("╔" + "═" * line + "╗")
        print(f"║{last}║")   
        print("╚" + "═" * line + "╝")         

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')  

ascii_art = pyfiglet.figlet_format("MULTIPLICATION TABLES")
print(ascii_art)
print("Type a number you want to learn its multiplication table!!")


while True:       
    print("===================================")
    num = int(input("Please input a number: "))
    print("===================================")
    calc(num)
    time.sleep(5)

    choice = input("Would You like to try again? (Y/N): ")
    
   
    if choice == "N":
        print("Thank you for using!")       
        break

    clear_screen()
                    