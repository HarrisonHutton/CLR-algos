"""
Exercise 2.1.2 in the book
"""

def bwardsinsertionsort(arr):
    n = len(arr)
    for j in range(n-2, -1, -1):
        key = arr[j]
        i = j+1
        while i <= n-1 and arr[i] > key:
            arr[i-1] = arr[i]
            i += 1
        arr[i-1] = key
