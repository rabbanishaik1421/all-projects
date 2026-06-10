def calculate_addition(a, b):
    return float(a)+float(b);

def calculate_subtraction(a, b):
    return a - b

def calculate_multiplication(a, b):
    return a * b

def calculate_division(a, b):
    return a / b

#power function
def calculate_power(a, b):
    return a ** b

#modulus function
def calculate_modulus(a, b):
    return a % b

while True:
    print("\n Data Calculator")
    print("\n 1. Addition")
    print("\n 2. Subtraction")
    print("\n 3. Multiplication")
    print("\n 4. Division")
    print("\n 5. Modulus")
    print("\n 6. Power")

    choice = int(input("Enter your choice:"))

    #Addition
    if choice == 1:
        a = float(input("Enter number 1: "))
        b = float(input("Enter number 2: "))

        sum = calculate_addition(a, b)
        print(sum)

    #subtraction
    elif choice == 2:
        a = float(input("Enter number 1: "))
        b = float(input("Enter number 2: "))

        sub = calculate_subtraction(a, b)
        print(sub)

    #multiplication
    elif choice == 3:
        a = float(input("Enter number 1: "))
        b = float(input("Enter number 2: "))

        mul = calculate_multiplication(a, b)
        print(mul)

    #division
    elif choice == 4:
        a = float(input("Enter number 1: "))
        b = float(input("Enter number 2: "))

        div = calculate_division(a, b)
        print(div)

    #modulus
    elif choice == 5:
        a = float(input("Enter number1: "))
        b = float(input("Enter number2 to get power: "))

        power = calculate_modulus(a, b)
        print(power)

    #power
    elif choice == 6:
        a = float(input("Enter number1: "))
        b = float(input("Enter number2 to get power: "))

        power = calculate_power(a, b)
        print(power)

    else:
        print("Entered wrong, choice! Please try again")

