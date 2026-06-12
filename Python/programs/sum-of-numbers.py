'''
Sum of numbers:
'''
from functools import reduce
nums = [3, 4, 5, 6, 8, 9]
result = reduce(lambda x, y:x+y, nums)
print(result)