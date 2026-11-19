'''
Problem Statement:
Given a number N, print their prime factors in sorted order.

Input Description:
The input consists of a number N, where 2 <= N <= 100000.

Sample Input:
18

Sample Output:
2 3
'''
prime_factors=[]
n=int(input())
for i in range(2, n):
    is_prime = True

    for j in range(2, i):
        if i % j == 0:
            is_prime = False
            break

    if is_prime:
        if n % i == 0:
            prime_factors.append(i)

if prime_factors:
    print(*prime_factors)
else:
    print(n)