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
    result = sum(nums)
    return result

#calculate average
def calculate_average(nums):
    result = sum(nums) / len(nums)
    return result

#Factorial of a number
def calculate_factorial(num):
    i=1
    factorial=1
    for n in range(i, num+1):
        factorial *=n
    
    return factorial

#Check prime
def check_prime(num):    
    if num < 2:
        return False
    
    for i in range(2, int(num ** 0.5)+1):
        if n % i == 0:
            return False
        
    return True

#Even or Odd
def check_evenorodd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
#Area of circle
def areaofcircle(num):
    return 3.14 * num * num

#Area of rectangle
def area_of_rectangle(l, w):
    return l * w

#Area of triangle
def area_triangle(b, h):
    return 0.5 * b * h

#Reverse number
def reverse_number(num):
    num = str(num)
    return num[::-1]

#Count numbers
def count_digits(num):
    num = str(num)
    return len(num)

#Sum of digits
def sum_of_digits(num):
    sum = 0
    num = str(num)
    nums =list(map(int, num.split()))
    i = 0
    while i<len(nums):
        sum += int(nums[i])
        i+=1
    
    return sum

#Check palindrome number
def check_palindrome(num):
    revnum = str(num)[::-1]
    if num == int(revnum):
        return True
    else:
        return False

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
    print("15. Average of numbers")
    print("16. Factorial of a number")
    print("17. Check prime or not")
    print("18. Even or odd")
    print("19. Area of circle")
    print("20. Area of rectangle")
    print("21. Area of triangle")
    print("22. Reverse number")
    print("23. Count numbers")
    print("24. Sum of digits")
    print("25. Check palindrome number")
    print("26. Exit")

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

    #average of numbers
    elif choice == 15:
        numbers = list(map(float, input("Enter numbers: ").split()))
        print("Minimum Value:", calculate_average(numbers))

    #average of numbers
    elif choice == 16:
        num = input("Enter number: ")
        result = calculate_factorial(num)
        print("Factorial:", result)
    
    #Check price
    elif choice == 17:
        num = int(input("Enter number:"))
        result = check_prime(num)
        print("Prime Number:", result)

    #Check Even or Odd
    elif choice == 18:
        num = int(input("Enter number:"))
        result = check_evenorodd(num)
        print("Even or Odd:", result)

    #Area of circle
    elif choice == 19:
        num = int(input("Enter number:"))
        result = areaofcircle(num)
        print("Area of circle", result)

    #Area of rectangle
    elif choice == 20:
        length = int(input("Enter length:"))
        width = int(input("Enter width:"))
        result = area_of_rectangle(length, width)
        print("Area of rectangle", result)

    #Area of triangle
    elif choice == 21:
        breadth = int(input("Enter breadth:"))
        height = int(input("Enter height:"))
        result = area_triangle(breadth, height)
        print("Area of triangle", result)

    #Reverse Number
    elif choice == 22:
        num = str(input("Enter number:"))
        revnum = num[::-1]
        print("Reverse number", revnum)

    #count numbers
    elif choice == 23:
        num = str(input("Enter number"))
        result = count_digits(num)
        print("Count of digits", result)

    #sum of digits
    elif choice == 24:
        num = str(input("Enter number"))
        result = sum_of_digits(num)
        print("Count of digits", result)

    #sum of digits
    elif choice == 25:
        num = str(input("Enter number"))
        result = check_palindrome(num)
        print("Palindrome", result)

    #Exit
    elif choice == 20:
        print("Thank you")
        break

    else:
        print("Entered wrong, choice! Please try again")

