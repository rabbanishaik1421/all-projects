'''
Problem Statement:
Write a code to get an integer N and print the sum of values from 1 to N.

Input Description:
A single line contains an integer N.

Output Description:
Print the sum of values from 1 to N.

Explanation:
The sum of values from 1-10 is 55.

Sample Input:
10

Sample Output:
55
'''
n = int(input())
sum=0
for i in range(1, n+1):
    sum += i

print(sum)  