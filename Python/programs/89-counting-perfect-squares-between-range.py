'''
Problem Statement:
Given a range (i.e) two numbers L and R count the number of perfect squares within the range (inclusive of L and R).If no perfect square exists within the range print '-1'.

Input Description:
The input consists of two integers L and R, representing the range, where L <= R <= 100000.

Output Description:
The output is an integer representing the count of perfect squares within the range [L, R], or -1 if none exist.

Sample Input:
2 10

Sample Output:
2
'''
nums = "2 3"
i, n = list(map(int, nums.split()))
squares = []
while i<n:
    sq = i**2
    if sq<n:
        squares.append(sq)
    i+=1

print(len(squares) if squares else -1)
