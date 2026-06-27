'''
284. Max Stock Profit

Problem Statement:
You have been given stock prices for next N days. Find out: max profit in buying and selling 1 share Condition: Share must be sold any day after buying date. Given a number N followed by N integers print the maximum profit.

Input Description:
The input consists of an integer N, followed by N integers representing the stock prices. N is at most 100000.

Output Description:
The output is the maximum profit that can be made.

Sample Input:
10
5 1 4 6 7 8 4 3 7 9

Sample Output:
8

Explanation:
For the given sample input, the minimum price is 1 and the maximum price after buying at 1 is 9, resulting in a maximum profit of 9 – 1 = 8.
'''
n=10
nums = "5 1 4 6 7 8 4 3 7 9"

nums = list(map(int, nums.split()))
# min_num = min(nums)
# max_num = max(nums)
# diff = max_num - min_num
# print(diff)
n = int(input())
prices = list(map(int, input().split()))

min_price = prices[0]
max_profit = 0

for price in prices:
    if price < min_price:
        min_price = price

    profit = price - min_price

    if profit > max_profit:
        max_profit = profit

print(max_profit)