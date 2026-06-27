'''
244. Find First Repeated Number

Problem Statement:
Given a number N followed by N numbers. Out of these N numbers some of them are repeated. Write a program to find the first number which is repeated. If no numbers are repeated print 'unique'.

Input Description:
The input consists of an integer N, followed by N numbers. The constraint for N is 1 <= N <= 100000.

Output Description:
The output should be the first number that is repeated. If no numbers are repeated, print 'unique'.

Sample Input:
7
1 2 3 2 3 4 3

Sample Output:
2
'''
n = int(input())
nums = list(map(int, input().split()))
seen_num=set()
for num in nums:
    if num in seen_num:
        print(num)
        break
        
    seen_num.add(num)
else:
    print('unique')