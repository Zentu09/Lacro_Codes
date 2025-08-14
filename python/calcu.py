import time

while True:   
        
    print("1. Use Addition")
    print("2. Use Subtraction")
    print("3. Use Multiplication")
    print("4. Use Division")

    choices = input("Please select: ")
    print()  # Mas maganda mag space dito instead sa java
    print()

    match choices:
        case "2":

            num1 = float(input("Please add the first number: "))
            num2 = float(input("Please add the second number: "))
            difference = num1 - num2
            print() 
            print(f"The answer is {difference}") 
            print()
            print()
            time.sleep(2)

        case "1":
            num1 = float(input("Please add the first number: "))
            num2 = float(input("Please add the second number: "))
            sum = num1 + num2
            print() 
            print(f"The answer is {sum}") 
            print()
            print()
            time.sleep(2)

        case "3":
            num1 = float(input("Please add the first number: "))
            num2 = float(input("Please add the second number: "))
            product = num1 * num2
            print() 
            print(f"The answer is {product}") 
            print()
            print()
            time.sleep(2)

        case "4":
            num1 = float(input("Please add the first number: "))
            num2 = float(input("Please add the second number: "))
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
            else:
                quotient = num1 / num2
                print()
                print(f"The answer is {quotient}")
            print()
            print()
            time.sleep(2)

        case _:
            print("Please input again")