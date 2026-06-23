'''
227. Max Meetings in One Room

Problem Statement:
There is one meeting room in Flipkart. There are n meetings in the form of (S [ i ], F [ i ]) where S [ i ] is start time of meeting i and F [ i ] is finish time of meeting i Given a number N followed by 2 arrays S and F of sizes N and N, What is the maximum number of meetings that can be accommodated in the meeting room assuming the room can only accommodate one meeting at a time.

Input Description:
The input consists of a number N followed by 2 arrays S and F of sizes N and N. N is between 1 and 100000 (inclusive).

Output Description:
The output is the maximum number of meetings that can be accommodated in the meeting room.

Sample Input:
3
10 12 30
20 25 30
'''
n=3
n=int(n)
nums1 = "10 12 30"
nums2 = "20 25 30"
n=6
nums1 = "1 3 0 5 8 5"
nums2 = "2 4 6 7 9 9"
n=3
nums1 = "1 4 6"
nums2 = "3 5 7"

s = list(map(int, nums1.split()))
f = list(map(int, nums2.split()))

meetings = []

for i in range(n):
    meetings.append((s[i], f[i]))

meetings.sort(key=lambda j: j[1])

count = 1
last_finish = meetings[0][1]

for i in range(1, n):
    if meetings[i][0] >= last_finish:
        count += 1
        last_finish = meetings[i][1]

print(count)

# s = list(map(int, nums1.split()))
# f = list(map(int, nums2.split()))

# meetings = list(zip(s, f))
# meetings.sort(key=lambda x: x[0])

# last_finish = meetings[0][1]

# count=1
# for i in range(1, n):
#     if meetings[i][0] > last_finish:
#         count+=1

# print(count)

# checked = []

# i=0
# while i < n:
#     if s[i] not in checked and s[i] > 0:
#         diff = int(s[i] - f[i])
        
#         if abs(diff)>0:
#             checked.append(s[i])

#     i+=1

# print(len(checked))
