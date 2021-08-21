#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

# first attempt
# this solution is too slow - a couple of test cases were complaining 'timeout'
# def superDigit(n, k):
#     # Write your code here
#
#     new_str = n * k
#     # if only 1 digit -> its super digit is itself
#     if len(new_str) == 1:
#         super_digit = int(new_str)
#         return super_digit
#     else:
#         sum = 0
#         for i in new_str:
#             sum += int(i)
#         sum_str = str(sum)
#             # print(sum)
#             # the commented out line below are not needed
#             # we can just use this function itself
#             # super_digit = 0
#             # for j in str(sum):
#             #     super_digit += int(j)
#         return superDigit(sum_str, 1)

# second attempt
# optimize based on the first attempt
def superDigit(n, k):
    # Write your code here

    # if only 1 digit -> its super digit is itself
    if len(n) == 1:
        super_digit = int(n)
        return super_digit
    else:
        sum = 0

        # avoid iterating the whole str
        for i in range(len(n)):
            sum += k * int(n[i])
        sum_str = str(sum)
            # print(sum)
            # the commented out line below are not needed
            # we can just use this function itself
            # super_digit = 0
            # for j in str(sum):
            #     super_digit += int(j)
        return superDigit(sum_str, 1) # this is important!! (no need to write endless loops in this function)

# print(superDigit('9857', 4))
# print(superDigit('148', 3))