'''
Problem Statement:
Write a code get an integer number as input and print the sum of the digits.

Input Description:
A single line containing an integer.

Output Description:
Print the sum of the digits of the integer.

Explanation:
1+2+4=7

Sample Input:
124

Sample Output:
7
'''
n = str(input())
i=0
sum=0
while i<len(n):
    sum = sum + int(n[i])
    i+=1
print(sum)