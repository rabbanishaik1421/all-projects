'''
Given 2 numbers N,M. Find their difference and check whether it is even or odd.


Sample Input:
5 5


Sample Output:
even
'''
nums = "7 4"
nums = list(map(int, nums.split()))
diff = nums[0] - nums[1]
if(diff % 2 == 0):
    print("even")
else:
    print("odd")
