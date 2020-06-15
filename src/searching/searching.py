def linear_search(arr, target):

    for ix, el in enumerate(arr):
        if el == target:
            return ix

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    lo, hi = 0, len(arr)-1
    while lo <= hi:
        mid = (lo + hi)//2
        if target < arr[mid]:
            hi = mid-1
        elif arr[mid] < target:
            lo = mid+1
        else:
            return mid

    return -1  # not found
