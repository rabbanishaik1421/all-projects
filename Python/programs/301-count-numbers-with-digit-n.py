'''
301. Count Numbers with Digit N

Problem Statement:
Given three numbers L,R,N, print the count of numbers with occurences of the number N in [L,R].

Input Description:
Input Size : 1 <= L,R,N <= 100000

Sample Input:
10 130 11

Sample Output:
11

Explanation:
11,110,111,112....119
'''
nums = "10 130 11"
L, R, N = list(map(int, nums.split()))
nums = []
while L<=R:
    if str(N) in str(L):
        nums.append(L)
    L+=1
    
print(len(nums))