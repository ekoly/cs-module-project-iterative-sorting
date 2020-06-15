# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):

    for ix in range(0, len(arr)-1):
        min_ix = ix
        for jx in range(ix+1, len(arr)):
            if arr[min_ix] > arr[jx]:
                min_ix = jx
        tmp = arr[ix]
        arr[ix] = arr[min_ix]
        arr[min_ix] = tmp

    return arr


def bubble_sort(arr):

    for _ in range(len(arr)):
        for ix, jx in zip(range(0, len(arr)-1), range(1, len(arr))):
            if arr[ix] > arr[jx]:
                tmp = arr[ix]
                arr[ix] = arr[jx]
                arr[jx] = tmp

    return arr

'''
STRETCH: implement the Count Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def count_sort(arr, maximum=10):

    buckets = [0 for _ in range(maximum+1)]
    for el in arr:
        if el < 0 or maximum < el:
            raise ValueError()
        buckets[el] += 1

    arr = [x for x, count in enumerate(buckets) for _ in range(count)]

    return arr
