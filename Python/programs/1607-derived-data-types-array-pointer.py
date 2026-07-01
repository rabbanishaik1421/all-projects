'''
Problem Statement:
You need to develop a program that processes and analyzes large datasets of integers. Your task is to manage data using arrays and pointers and perform operations like sorting, searching, and finding the median.

Requirements
Data Input: There will be an Input of the array of integers dynamically.
Sorting: Sort the array using the quicksort algorithm with pointers.
Searching: Implementing the binary search methodology using pointers to find a specific element.
Median Calculation: Calculate the median of the sorted array using pointers.

Input Format
The first line will contain an integer n, such that 1 <= n <= 100000, representing the number of elements in the array.
The second line contains n space-separated integers representing the array elements.
The third line contains an integer x, representing the element to search in the array.

Output Format
Print the sorted array of integers on a single line, space-separated.
Print the median value of the array on the next line.
Print the result of the binary search on the next line: the index of the element x if found, otherwise -1.

Constraints
All integers are within the range -1000000 to 1000000.
Efficient use of pointers for sorting, searching, and calculating the median.
Consider both odd and even lengths for median calculation.

Example
Input:
7
12 4 5 3 8 7 1
5

Output:
1 3 4 5 7 8 12
5
3
'''
def quick_sort(arr):
    length = len(arr)
    if length <= 1:
        return arr
    else:
        pivot = arr.pop()

    items_greater = []
    items_lower = []

    for item in arr:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)

    return quick_sort(items_lower)+[pivot]+quick_sort(items_greater)
    

n=7
nums = "12 4 5 3 8 7 1"
s=5

arr = list(map(int, nums.split()))
sortarr = quick_sort(arr)
print("Sorted Array:", " ".join(map(str, sortarr)))
print("Binary Search Result:", sortarr.index(s)+1)