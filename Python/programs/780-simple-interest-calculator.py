'''
Problem Statement:
You are given with Principle amount($), Interest Rate(%) and Time (years) in that order. Find Simple Interest. Print the output up to two decimal places (Round-off if necessary). (S.I. = PTR/100)

Input Description:
Three values are given to you as the input. these values correspond to Principle amount, Interest Rate and Time in that particular order.

Output Description:
Find the Simple interest and print it up to two decimal places. Round off if required.

Explanation:
P = 1000 $
T = 2 Years
R = 5 %
S.I. = 100025/100 = 100.00

Sample Input:
1000 2 5

Sample Output:
100.00
'''
p, t, r = list(map(float, input().split()))
simple_interest = (p * t * r) / 100
simple_interest = round(simple_interest, 2)
#print(simple_interest)
print(f"{simple_interest:.2f}")