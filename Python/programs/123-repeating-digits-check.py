'''
123. Repeating Digits Check

Given a number N,check whether it has repeating digits in it.print 'yes' if it has repeating digits otherwise print 'no'.

Sample Input:
11234

Sample Output:
yes
'''
nums = 11234
nums = str(nums)
#nums = list(map(int, nums.split()))
freq={}
for i in range(len(nums)):
    #print(i)
    #print(nums[i])
    freq[nums[i]]=freq.get(nums[i],0)+1

print("yes" if max(freq.values())>1 else "no")
