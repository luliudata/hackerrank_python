#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#
# import numpy as np


def countingSort(arr: list):
    # Write your code here
    # https://stackabuse.com/counting-sort-in-python
    # initiate counter array
    # counter_arr = np.zeros(100) # can't import numpy in Hackerrank
    counter_arr = [0] * 100

    for i in range(len(arr)):
        for j in range(len(counter_arr)):
            # Find the index in the count array that is equal to the value of the current element arr[i]
            if arr[i] == j:
                counter_arr[j] += 1
    return counter_arr

# print(countingSort([1,1,3,2,1]))