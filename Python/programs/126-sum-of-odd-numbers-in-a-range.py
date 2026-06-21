'''
126. Sum of Odd Numbers in a Range

Problem Statement:
Given a range[L,R], print the sum of all the odd numbers within the range(inclusive of L and R).

Sample Input:
5 10

Sample Output:
21
'''
nums = "5 10"
nums = "7 9"
#nums = "5 7"
n1, n2 = list(map(int, nums.split()))
# sum=0
# for n in range(n1, n2+1):
#     if n % 2 != 0:
#         sum += n

#Using List comprehension
sumofdigits = sum([n for n in range(n1, n2+1) if (lambda x: x % 2 != 0)(n) ])

#using filter and lambda
sumofdigits = sum(filter(lambda x: x % 2 != 0, range(n1, n2+1)))
print(sumofdigits)