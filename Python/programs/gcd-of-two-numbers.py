'''
Problem Statement:
Given 2 numbers N,M find the GCD of N and M.If it cannot be found for given number(s) then print -1


Sample Input:
10 5


Sample Output:
5
'''
i=1
num1 = 10
list1= []
while i<=num1:
    if(num1 % i == 0):
        list1.append(i)
    i=i+1

i=1
num2 = 5
list2= []
while i<=num2:
    if(num2 % i == 0):
        list2.append(i)
    i=i+1

common = list(set(list1) & set(list2))
print(max(common))