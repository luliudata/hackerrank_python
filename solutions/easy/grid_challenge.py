#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#

def gridChallenge(grid):
    # Write your code here
    for i in range(len(grid)): #4 rows / 3cols (len(grid[i)
        grid[i]=''.join(sorted(grid[i]))
        print(f"grid[i] is: {grid[i]}")

    col = []
    col_sorted = []
    for a in range(len(grid[i])):
        temp_col = [] # add each element in each column
        for b in range(len(grid)):
            temp_col.append(grid[b][a])
            # print(temp_col)
        col.append(''.join(temp_col))
        # print(col)

        col_sorted.append(''.join(sorted(temp_col)))

    if col != col_sorted:
        return 'NO'
    else:
        return 'YES'



import numpy as np
# grid = ['abc', 'def', 'opq', 'xyz']
# print(gridChallenge(grid))
