import os


def rose_love(input_string):
    input_lower = input_string
    
    if input_lower == "Rose":
        print("best")
        
    elif input_lower == "rose":
        print("make it big") 
                     
    else:
        print(f"Rose not! not{input_string}")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')      
        
if __name__ == "__main__":
    while True:
        user_input = input("Enter word: ")
        rose_love(user_input)

        again = input("Would you like to do it again? (Y/N): ").strip().lower()
        
        if again == "N":
            clear_screen()
            break

        while True:
            if again == "Y":
                clear_screen()
                break       
            else:
                print("Wrong input try")
                break
        
        


        


    
        
       