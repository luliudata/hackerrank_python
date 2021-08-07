#
# Complete the 'towerBreakers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#

def towerBreakers(n: int, m: int) -> int:
    # Write your code here
    if m == 1 or n % 2 == 0:
        return 2
    else:
        return 1
