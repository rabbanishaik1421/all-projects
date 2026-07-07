'''
165. Power of Two Check

Problem Statement:
Given a number N, check whether it is a power of 2.

Sample Input:
2048

Sample Output:
yes
'''
num = int(input())
# print("yes" if num % 2 == 0 else "no")
# if n ** 2 
while num>1:
    if num % 2 != 0:
        print("no")
        break
    
    num //=2
else:
    print("yes")