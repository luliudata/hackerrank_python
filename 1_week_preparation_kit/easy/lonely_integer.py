#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

from collections import Counter


#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a: list) -> str:
    # Write your code here

    for freq in Counter(a).items():
        if freq[1] == 1:
            return freq[0]
    return None


# print(lonelyinteger([1,2,3,4,3,2,1]))