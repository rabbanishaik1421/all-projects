'''
99. Prime Pairs for a Number

Problem Statement:
Given a number N, print the distinct pairs formed by multiplying two prime numbers (i.e)prime x prime should yield the N.Also print the numbers in descending order.If no such pairs can be formed print '-1'.

Input Description:
The input consists of a single integer N, where 1 <= N <= 100000.

Output Description:
Print the distinct pairs of prime numbers (prime x prime = N) in descending order. If no such pairs can be formed, print '-1'.

Sample Input:
65

Sample Output:
13 5
'''
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


n = int(input())
found = False

for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
        j = n // i

        if is_prime(i) and is_prime(j):
            print(max(i, j), min(i, j))
            found = True
            break

if not found:
    print(-1)