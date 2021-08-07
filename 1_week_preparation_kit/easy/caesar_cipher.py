#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#
import string

symbols_low = string.ascii_lowercase
# print(symbols_low)
symbols_up = string.ascii_uppercase


def caesarCipher(s: str, k: int) -> str:
    # Write your code here
    res = []
    for letter in s:
        if letter.isupper():
            # adding '% len(symbols_up)]' is to
            # avoid IndexError: string index out of range
            res.append(symbols_up[(symbols_up.index(letter) + k) % len(symbols_up)])
        elif letter.islower():
            res.append(symbols_low[(symbols_low.index(letter) + k) % len(symbols_low)])
        else:
            res.append(letter)

    return "".join(map(str, res))

# print(caesarCipher('middle-Outz', 2))
print(caesarCipher('Hello_World!', 4))