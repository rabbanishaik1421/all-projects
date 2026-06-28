'''
Problem Statement:
Given a number N, find the sum of prime numbers that end with 3 from 2 to N.

Input Description:
The input consists of a single integer N, where N <= 100000.

Output Description:
The output is the sum of prime numbers that end with 3, from 2 to N.

Sample Input:
5

Sample Output:
3
'''
n=5
total = 0
for num in range(2, n+1):
    if num % 10 == 3:
        is_prime = True

        if num < 2:
            is_prime = False
        else:
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break
        if is_prime:
            total += num

print(total)
