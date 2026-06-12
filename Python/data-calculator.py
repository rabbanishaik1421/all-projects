import math
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

#square root
def calculate_squareroot(a):
    return math.sqrt(a)

#sin tita function to get result
def calculate_sinval(a):    
    return math.sin(a)

#cos tita function to get result
def calculate_cosval(a):    
    return math.cos(a)

#tan tita function to get result
def calculate_tanval(a):    
    return math.tan(a)

#calculate percentage
def calculate_percentage(n, p): 
    percentage = (p/100) * n
    return percentage

#calculate max
def calculate_max(a):    
    return max(a)

#calculate max
def calculate_min(a):    
    return min(a)

#calculate sum
def calculate_sum(nums):
    from functools import reduce

    result = reduce(lambda x, y:x+y, nums)
    return result

while True:
    print("\n Data Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Power")
    print("7. Square Root")
    print("8. Sin tita")
    print("9. Cos tita")
    print("10. Tan tita")
    print("11. Percentage")
    print("12. Max value")
    print("13. Min value")
    print("14. Sum of numbers")

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

    #square root
    elif choice == 7:
        a = float(input("Enter number: "))

        square_root = calculate_squareroot(a)
        print(square_root) 

    #calculate the sin tita value
    elif choice == 8:
        a = float(input("Enter number: "))

        sinval = calculate_sinval(a)
        print(sinval)    

    #calculate the cos tita value
    elif choice == 9:
        a = float(input("Enter number: "))

        cosval = calculate_cosval(a)
        print(cosval)    

    #calculate the tan tita value
    elif choice == 10:
        a = float(input("Enter number: "))

        tanval = calculate_tanval(a)
        print(tanval)    

    #calculate the tan tita value
    elif choice == 11:
        n = float(input("Enter number: "))
        p = float(input("Enter percentage: "))

        percentage = calculate_percentage(n, p)
        print(percentage)    

    #calculate the max value
    elif choice == 12:
        numbers = list(map(float, input("Enter numbers: ").split()))
        print("Maximum Value:", calculate_max(numbers))

    #calculate the max value
    elif choice == 13:
        numbers = list(map(float, input("Enter numbers: ").split()))
        print("Minimum Value:", calculate_min(numbers))

    #sum of numbers
    elif choice == 14:
        numbers = list(map(float, input("Enter numbers: ").split()))
        print("Minimum Value:", calculate_sum(numbers))

    else:
        print("Entered wrong, choice! Please try again")

