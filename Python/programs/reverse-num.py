'''
Write a function to reverse the given integer and print the reversed integer.

Input:

An integer num (-10^9 ≤ num ≤ 10^9).

Output:

Print the reversed integer.

Sample Input:

12345

Sample Output:

54321
'''

num = 12345
revnum = str(num)[::-1]
print(revnum)