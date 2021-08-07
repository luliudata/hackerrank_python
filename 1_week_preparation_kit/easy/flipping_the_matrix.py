#
# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#


def flippingMatrix(matrix) -> int:
    # Write your code here
    n = len(matrix)
    s = 0

    # x = 5 / 2  # 2.5
    # y = 5 // 2  # 2
    for i in range(n // 2):
        for j in range(n // 2):
            s += max(matrix[i][j], matrix[i][n - j - 1], matrix[n - i - 1][j], matrix[n - i - 1][n - j - 1])
    return s

import numpy as np

a = np.array([[1,2],
              [3,4]])
print(flippingMatrix(a))