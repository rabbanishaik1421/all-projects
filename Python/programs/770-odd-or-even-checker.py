'''
770. Odd or Even Checker

Problem Statement:
You are provided with a number check whether its odd or even.
Print "Odd" or "Even" for the corresponding cases.
Note: In case of a decimal, Round off to nearest integer and then find the output. Incase the input is zero, print "Zero".

Input Description:
A number is provided as the input.

Output Description:
Find out whether the number is odd or even.
Print "Odd" or "Even" for the corresponding cases.
Note: In case of a decimal, Round off to nearest integer and then find the output. In case the input is zero, print "Zero".

Explanation:
2%2 = 0.
2 is an even number.

Sample Input:
2

Sample Output:
Even
'''
n = float(input())
n = round(n)
if n>0:
    print("Even" if n % 2 == 0 else "Odd")
else:
    print("Zero")