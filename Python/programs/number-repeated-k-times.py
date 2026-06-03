'''
47. Numbers Repeated K Times

Problem Statement:
Given 2 numbers N,K and an array of N elements, print the number(s) that has been repeated K times.Print them in ascending order if there are more than one number to be printed.If no element satisfies the pattern then print -1


Input Description:
The input consists of two integers N and K, followed by an array of N elements. N and K are up to 100000.


Output Description:
Print the numbers that have been repeated K times in ascending order. If no such element exists, print -1.


Sample Input:
5 2
1 2 4 1 2
'''
num = "4 2"
numarr = "3 2 4 1 5"
N, K = list(map(int, num.split()))
arr = list(map(int, numarr.split()))

#solution 1
'''
repeatarr = set()
print("K", K)
i=0
while i < N:
    j=0
    count=0
    while j < N:
        if arr[i] == arr[j]:
            count += 1
            
            if count == K:
                print("Count", count)
                repeatarr.add(arr[i])
            
        j+=1
    i+=1

if len(repeatarr)>=1:
    print(*repeatarr)
else:
    print(-1)
'''

#solution 2
freq = {}

for num in arr:
    freq[num] = freq.get(num, 0)+1

#print(freq)

result = []
for num, count in freq.items():
    if count == K:
        result.append(num)

if result:
    print(*sorted(result))
else:
    print(-1)