#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#
import numpy as np

def diagonalDifference(arr) -> int:
    # Write your code here
    lr_diag_sum = 0
    rl_diag_sum = 0

    for i in range(len(arr)):
        for j in range(len(arr)):
            # condition to find left-to-right diagonal
            if i == j:
                lr_diag_sum += arr[i][j]
            # condition to find right-to-left diagonal
            if (i + j) == (len(arr) - 1): #note here don't use elif
                rl_diag_sum += arr[i][j]

    return abs(lr_diag_sum - rl_diag_sum)


a = np.array([[11, 2, 4],
              [4, 5, 6],
              [10, 8, -12]])
# print(len(a))  # 3
print(diagonalDifference(a))