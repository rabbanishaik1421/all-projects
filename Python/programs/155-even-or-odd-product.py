'''
Problem Statement:
Given a number N and an array of N integers, predict if the product of all elements would be even or odd(actual multiplication may lead to overflows ai <= 100000000).If there is only one element present in the array print whether that number is odd or even.

Input Description:
The input consists of a number N, followed by an array of N integers. N is up to 100000.

Output Description:
The output should be 'even' or 'odd', indicating whether the product of all elements is even or odd. If there is only one element, it indicates whether that single element is odd or even.

Sample Input:
4
2 4 4 2

Sample Output:
even
'''
num = int(input())
nums = list(map(int, input().split()))
import math
product = math.prod([x for x in nums])
print("even" if product % 2 == 0 else "odd")