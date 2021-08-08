#
# Complete the 'palindromeIndex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

# https://www.hackerrank.com/challenges/palindrome-index/editorial
# TODO - This solution needed to be verified again
def palindromeIndex(s: str) -> int:
    # Write your code here
    # looking at it from both ends just like you would while checking for the string being a palindrome.
    # When an inequality occurs
    # -> skip the right element and check the middle portion of the string including the left element
    # if it's a palindrome -> if a palindrome index of right element should be skipped
    # -> else index of left element should be skipped
    # If no inequaliry occured then return -1.

    #https://stackoverflow.com/questions/509211/understanding-slice-notation
    for i in range(len(s)//2):
        if s[i] != s[len(s) - i - 1]:
            # skip the right element
            new_str = s[:len(s) - i - 1]
            if new_str[:] == new_str[::-1]: # check if it's a palindrome
                return i
            return len(s) - i - 1
    return -1

    # for i in range(len(s) // 2):
    #     if s[i] != s[-(i + 1)]:
    #         newstr = s[:i] + s[i + 1:]
    #         if newstr[:] == newstr[::-1]:
    #             return i
    #         return -(i + 1) + len(s)
    # return -1

# print(palindromeIndex('abab'))
print(palindromeIndex('abab'))
# s = 'abab'
# new_str=s[:3]
# print(new_str[:])
# print(new_str[::-1])
