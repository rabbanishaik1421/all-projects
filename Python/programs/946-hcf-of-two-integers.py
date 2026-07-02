'''
Problem Statement:
Write a code to get 2 integers as input and find the HCF of the 2 integer without using recursion or Euclidean algorithm.

Input Description:
A single line containing 2 integers separated by space.

Output Description:
Print the HCF of the integers.

Explanation:
The HCF of 2 and 3 is 1 as they are prime numbers.

Sample Input:
2 3

Sample Output:
1
'''
a, b = list(map(int, input().split()))
smaller = min(a, b)

for i in range(smaller, 0, -1):
    if a % i == 0 and b % i == 0:
        print(i)
        break