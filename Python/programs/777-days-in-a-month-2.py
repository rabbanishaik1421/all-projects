'''
Problem Statement:
You will be provided with a number. Print the number of days in the month corresponding to that number. Note: In case the input is February, print 28 days. If the Input is not in valid range print "Error".

Input Description:
The input is in the form of a number.

Output Description:
Find the days in the month corresponding to the input number.
Print Error if the input is not in a valid range.

Explanation:
8 corresponds to august month.
There are 31 days in the month of August.

Sample Input:
8

Sample Output:
31
'''
n = int(input())
if n < 1 or n > 12:
    print("Error")
elif n == 2:
    print(28)
elif n in [4, 6, 9, 11]:
    print(30)
else:
    print(31)    