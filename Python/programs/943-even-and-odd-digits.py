'''
Problem Statement:
Write a code get an integer number as input and print the odd and even digits of the number separately.

Input Description:
A single line containing an integer.

Output Description:
Print the even and odd integers of the integer in a separate line.

Sample Input:
1234

Sample Output:
2 4
1 3

Explanation:
4 and 2 are even, 3 and 1 are odd.
'''
nums = str(input())
evenlist=[]
oddlist = []
i=0
while i<len(nums):
    if int(nums[i]) % 2 == 0:
        evenlist.append(nums[i])
    else:
        oddlist.append(nums[i])
    i+=1
    
print(*sorted(evenlist))
print(*sorted(oddlist))