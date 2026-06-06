'''
Problem Statement:
Given a range of 2 numbers (i.e) L and R count the number of prime numbers in the range (inclusive of L and R ).


Input Description:
Input Size : L <= R <= 100000(complexity O(n) read about Sieve of Eratosthenes)


Sample Input:
2 5


Sample Output:
3
'''
nums = "2 5"
count=0
n1, n2 = list(map(int, nums.split()))
for n in range(n1, n2):
    if n>1:
        isprime=True
        for i in range(2, n):
            if n % i == 0:
                isprime=False

        if isprime == True:
            count+=1

print(count)