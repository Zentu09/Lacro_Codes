import time                  # I want delays sir para mabasa muna yung print
import pyfiglet

ascii_art = pyfiglet.figlet_format("WELCOME PERPETUALITES")
print(ascii_art)

while True:   # i added while loop sa main menu para pwede ulit gamitn as well may purpose ang option 4

    print("===================================")
    print("1. Tell me your name")
    print("2. Use Addition")
    print("3. Guess my Lucky Number (1-50)")
    print("4. Exit")
    print("===================================")
    choices = input("Please select (1-4): ")
    print("===================================")
    print()                   # Mas maganda mag space dito instead sa java
    print()

    match choices:
        case "1":

                name = input("Please state your name: ")
                ascii_art = pyfiglet.figlet_format(f"{name}")
                ascii_hello = pyfiglet.figlet_format("HELLO")  # naka separate para pag nag print the name can be different anytime
                print(f"{ascii_hello}{ascii_art}")                                         
                print()
                print()
                time.sleep(2)

        case "2":
            num1 = float(input("Please add the first number: "))
            num2 = float(input("Please add the second number: "))
            sum = num1 + num2
            print() 
            print(f"The answer is {sum}") 
            print()
            print()
            time.sleep(2)

        case "3":
            myluckynumber = 21

            for attempt in range(15):
                guess = int(input("Please guess my lucky number!! (1-50): "))  

                try:
                             
                    if guess == myluckynumber:
                        print("You've guessed my lucky number CONGRATS!!")
                        time.sleep(2)
                        print()
                        print()
                        break                       
                    elif guess in range(myluckynumber -4, myluckynumber + 4): #to help the user know po na they are close sa lucky number
                        print("You're getting close!")
                        print()
                        time.sleep(2)                                      
                    elif guess > 24:
                        print("Your guess is too high!")
                        print()
                        time.sleep(2)                        
                    elif guess < 17:
                        print("Your guess is too low!")
                        print()
                        time.sleep(2) 

                except ValueError:
                    print("that is not a number!")                          


            else:
                print("Guess too many wrong. Now deleting you IRL")         
                                               

        case "4":
            print("Thank you for using!!")     
            break       

        case _:
            print("Please input again")
            time.sleep(2)
        

    

