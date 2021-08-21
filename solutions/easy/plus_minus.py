def plusMinus(arr: list):
    # Write your code here
    num = len(arr)
    num_p = 0
    num_n = 0

    for i in arr:
        if i > 0:
            num_p += 1
        elif i < 0:
            num_n += 1
        i += 1

    # https://stackoverflow.com/questions/9415939/how-can-i-print-many-significant-figures-in-python
    ratio_p = num_p / num
    ratio_n = num_n / num
    ratio_zero = 1 - ratio_p - ratio_n

    print('%.6f' % ratio_p + '\n' + '%.6f' % ratio_n + '\n' '%.6f' % ratio_zero)


# plusMinus([1, 1, 0, -1, -1])
# plusMinus([-4,3, -9, 0, 4, 1])
