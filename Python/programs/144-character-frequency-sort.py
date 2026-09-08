'''Problem Statement:
Given an array of N elements.find the number of occurences of each character and print it in the decreasing order of occurences, if 2 or more number occurs the same number of times, print the numbers in decreasing order.

Input Description:
Input Size : |N| <= 100000

Sample Input:
5
3 3 4 4 7

Sample Output:
4 3 7'''

n = int(input())
nums = list(map(int, input().split()))

freq = {}

for num in nums:
    freq[num] = freq.get(num, 0) + 1

result = sorted(freq.items(), key=lambda x: (x[1], x[0]), reverse=True)
res = []
for num, count in result:
    res.append(num)
    
print(*res)