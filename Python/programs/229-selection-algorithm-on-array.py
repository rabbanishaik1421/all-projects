'''
229. Selection Algorithm on Array

Problem Statement:
Given a number N and an array of N elements, a selection algorithm is implemented on this array where numbers at even position would be chosen, the algorithm is again and again implemented on the newly chosen array until only 1 element is remaining. Print the original position(index) of this element in the initial array.

Input Description:
The input consists of a number N and an array of N elements. Input Size: 1 <= N <= 100000.

Output Description:
The output is the original position(index) of the remaining element in the initial array.

Sample Input:
6
1 2 3 4 5 6

Sample Output:
3
'''
nums = "1 2 3 4 5 6"
nums = "3 2 4"
nums = "21 32 75 90 12 66 234 111 2 91"
nums = list(map(int, nums.split()))
count = 1
evenpos = []
for n in nums:
    if count % 2 == 0:
        evenpos.append(n)
    count+=1        

print(len(evenpos))