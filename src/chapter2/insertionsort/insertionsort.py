def insertionsort(arr: [int]) -> [int]:
    n = len(arr)
    for j in range(1, n):
        key = arr[j]
        i = j-1
        while i >= 0 and arr[i] > key:
            arr[i+1] = arr[i]
            i -= 1
        arr[i+1]=key
