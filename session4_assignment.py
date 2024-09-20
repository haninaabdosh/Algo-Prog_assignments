def add(x, y):
    return (x + y)

def subtract(x, y):
    return (x - y)

def multiply(x, y):
    return (x * y)

def divide(x, y):
    num_1 = eval(input("Enter the first number: "))
    num_2 = eval(input("Enter the second number: "))

#Selecting operations
print("Select the option")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exit")

while True:
    # Taking input from user
    select = eval(input("Select operations from (1/2/3/4/5): "))
    x = eval(input("Enter the first number: "))
    y = eval(input("Enter the second number: "))

    # Checking if the selected operation is valid
    if select in (1, 2, 3, 4, 5):
        if select == 1:
            print(f"{x} + {y} = {add(x, y)}")
        elif select == 2:
            print(f"{x} - {y} = {subtract(x, y)}")
        elif select == 3:
            print(f"{x} * {y} = {multiply(x, y)}")
        elif select == 4:
            try:
                print(f"{x} / {y} = {divide(x, y)}")
            except ZeroDivisionError:
                print("You can't divide by zero!")
        elif select ==5:
            print("Thank you!")
            exit()
    else:
        print("Invalid input, please select a valid operation.")