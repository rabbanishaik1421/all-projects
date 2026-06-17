'''
110. Divisibility Check of a Number

Problem Statement:
Given a number N, check if N is divisible by any number less than N (ie.,it leaves no remainder)except 1.

Input Description:
Input Size : 1 <= N <= 100000

Sample Input:
10

Sample Output:
yes
'''

n=10
found = "no"
if n<=1:
    print("no")
else:
    for i in range(2, n +1):
        if n % i == 0 and n != i:
            found="yes"
            break

print(found)