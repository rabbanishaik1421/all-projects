'''
Problem Statement:
Given 2 numbers A,B. Print the GCD of A! and B!.

Sample Input:
4 2

Sample Output:
2
'''
n, k = list(map(int, input().split()))
num = min(n, k)
fact = 1
for i in range(1, num+1):
    fact = fact * i
print(fact)