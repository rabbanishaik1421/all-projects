'''
32. Sum of First K Natural Numbers

Geekoin20
Easy
Topics
Problem Statement:
Write a program to print the sum of the first K natural numbers.


Input Description:
Input Size : n <= 100000


Sample Input:
3


Sample Output:
6
'''
n=3
sum=0
i=1
while(i<=n):
    sum = sum+i
    i +=1
print(sum)
