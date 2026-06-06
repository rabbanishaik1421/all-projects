'''
Problem Statement:
Given an array of N elements which follows either even number or odd number series.There may exists at maximum 1 even number in the odd series or 1 odd number in the even series.Find the different number if exists otherwise print '-1'?

Input Description:
Input Size : |N| <= 100000

Sample Input:
5
1 3 4 5 7

Sample Output:
4
'''
n=5
nums = "1 3 5 7 9"
arr = list(map(int, nums.split()))
even = []
odd = []
for k in arr:
    if k % 2 == 0:
        even.append(k)
    else:
        odd.append(k)

if len(even) == 1:
    print(*even)
elif len(odd) == 1:
    print(*odd)
else:
    print(-1)