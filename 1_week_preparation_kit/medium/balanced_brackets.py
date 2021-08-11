#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

# There are three types of matched pairs of brackets: [], {}, and ().
# By this logic, we say a sequence of brackets is balanced if the following conditions are met:
#
# -> It contains no unmatched brackets.
# -> The subset of brackets enclosed within the confines of a matched pair of brackets is
# also a matched pair of brackets.
def isBalanced(s: str) -> bool:
    # Write your code here
    while len(s) > 0:
        new_str = s
        # replace all the '[]'/'()'/'{}' with ''
        # if the string is unblanced, it'll remain the same
        s = s.replace('[]', '')
        s = s.replace('()', '')
        s = s.replace('{}', '')
        if new_str == s:
            return False
    return True

# print(isBalanced('[([{])]'))
# s = '[([{])]'
# s = s.replace('[]', '')
# print(s)
# s = s.replace('()', '')
# s = s.replace('{}', '')
# s = s.replace('[]', '')
# print(s)