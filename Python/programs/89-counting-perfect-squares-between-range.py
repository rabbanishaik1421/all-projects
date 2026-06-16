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
nums = "2 10"
i, n = list(map(int, nums.split()))
count=0
for j in range(i, n+1):
    sq = j ** 2
    if sq > j and sq<n:
        count+=1
    j+=1

print(count if count>0 else -1)