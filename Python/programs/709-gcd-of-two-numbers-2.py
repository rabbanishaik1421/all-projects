'''
Problem Statement:
Write a program to find the GCD of two numbers

Input Description:
Input contains two integers separated by space

Output Description:
print the GCD of two numbers

Sample Input:
28690 5126

Sample Output:
2

Explanation:
2
'''
num1, num2 = map(int, input().split())

div1 = [i for i in range(1, num1 + 1) if num1 % i == 0]
div2 = [i for i in range(1, num2 + 1) if num2 % i == 0]

common = set(div1) & set(div2)

print(max(common))