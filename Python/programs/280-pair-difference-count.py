'''
280. Pair Difference Count

Problem Statement:
Given a number N followed by an unsorted array of N numbers and a number K, find if there exists a pair of elements in the array whose difference is K. Return count of such pairs.

Input Description:
Input Size : N <= 100000

Output Description:
The count of pairs whose difference is K.

Sample Input:
6 4
8 12 16 4 0 20

Sample Output:
5
'''
nums1 = "6 4"
nums2 = "8 12 16 4 0 20"
nums1 = "5 3"
nums2 = "1 5 3 4 2"

nums1 = "4 5"
nums2 = "1 2 3 4"

n, k = list(map(int, nums1.split()))
nums2 = list(map(int, nums2.split()))

i=0
count=0
while i < len(nums2):
    j = i+1
    while j<len(nums2):
        diff = abs(int(nums2[i]) - int(nums2[j]))
        if diff == k:
            count+=1
        j+=1
    i+=1

print(count)