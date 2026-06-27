'''
389. Mirror String Pairs

Problem Statement:
Given an array of pairs of strings, find if there are mirror pairs. (s1, s2) & (s3, s4) are mirror pairs, if s1 = s4 and s2 = s3. The first string in each pair is distinct.

Input Description:
The first line contains the number string pairs N.
Then N string pairs follow.

Output Description:
Print YES, if a mirror pair exists, print NO otherwise.

Explanation:
(raja, kili) and (kili, raja) are mirror pairs

Sample Input:
3
raja kili
pan quil
kili raja

Sample Output:
YES
'''
n=int(input())
string1 = list(map(str, input().split()))
i=1 
found = "NO"
while i<n:
    string2 = list(map(str, input().split()))
    if string1[0] == string2[1] and string1[1] == string2[0]:
        found = "YES"
    i+=1
    
print(found)