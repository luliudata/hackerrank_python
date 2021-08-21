def findMedian(arr: list) -> int:
    # Write your code here
    sorted_arr = sorted(arr)
    median_index = len(arr) // 2

    median = sorted_arr[median_index]

    return median


# print(findMedian([1,3,5,7,9]))
# print(7//2)