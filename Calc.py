# My calculator
answer = input("what would you like to do?")
variable = 10

def add():
    number1 = input("Please enter the first number: ")
    number1 = int(number1)

    number2 = input("Please enter the second number: ")
    number2 = int(number2)

    total = number1 + number2

    print(total)

def subtract():
    number1 = input("Please enter the first number: ")
    number1 = int(number1)

    number2 = input("Please enter the second number: ")
    number2 = int(number2)

    total = number1 - number2

    print(total)

def multiply():
    number1 = input("Please enter the first number: ")
    number1 = int(number1)

    number2 = input("Please enter the second number: ")
    number2 = int(number2)

    total = number1 * number2

    print(total)

def divide():
    number1 = input("Please enter the first number: ")
    number1 = int(number1)

    number2 = input("Please enter the second number: ")
    number2 = int(number2)

    total = number1 / number2

    print(total)

while variable>=10:   

    if answer == "add":
        add()

    if answer == "subtract":
        subtract()

    if answer == "multiply":
        multiply()

    if answer == "divide":
        divide()

    if answer == "exit":
        variable = 5

print("Bye for now!")

