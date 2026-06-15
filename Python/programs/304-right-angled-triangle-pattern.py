'''
Right-Angled Triangle Pattern

Problem Statement:
Given a number N print a right angled traingle structure with the starting level as single 1 and every immediate proceeding level with 2 more additional ones than the previous level .Repeat the pattern for N levels.

Input Description:
Input Size : N <= 1000

Sample Input:
3

Sample Output:
1
1 1 1
1 1 1 1 1
'''

n=int(input())
for i in range(n):
    j=0
    lines=[]
    while j< (2*i + 1):
        #print(1, end=" ")
        lines.append(1)
        j+=1
    
    print(*lines)