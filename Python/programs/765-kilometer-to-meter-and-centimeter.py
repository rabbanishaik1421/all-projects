'''
Problem Statement:
You are given a number A in Kilometers. Convert this into B: Meters and C: Centi-Metres.

Input Description:
A number "A" representing some distance in kilometer is provided to you as the input.

Output Description:
Convert and print this value in meters and centimeters.

Explanation:
1 KM = 1000 M
1M = 100 CM
1KM = 1000*100 CM = 100000 CM

Sample Input:
2

Sample Output:
2000200000
'''
n = 2
km = n * 1000
meters = n * 100000
print(km)
print(meters)