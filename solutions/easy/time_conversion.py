def timeConversion(s: str) -> str:
    # Write your code here
    hh = int(s[:2])
    symbol = s[-2:]

    if symbol == 'PM' and 12 > hh >= 0:
        hh += 12
        new_s = str(hh) + s[2:-2]
    elif symbol == 'AM' and hh == 12:
        hh -= 12
        new_s = str(hh)+'0' + s[2:-2]
    else:
        new_s = s[:-2]

    return new_s


print(timeConversion('02:01:00PM'))
print(timeConversion('12:01:00PM'))
print(timeConversion('12:01:00AM'))
print(timeConversion('06:40:03AM'))

# s = '12:01:00PM'
# print(s[:2])  # hh
# print(s[2:-2])  #:01:00
# print(s[:-2])  #time
