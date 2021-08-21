# Zigzag sequences are a curious kind of integer sequence. They are sequences of at least
# length 3 that have the following form every three consecutive integers ai,ai+1,ai+2:
# ai < ai+1 > ai+2 or ai > ai+1 < ai+2
# Examples of zigzag sequences are 14, 17, 3, 19 and 1, 7, 1, 97, 2.
# Examples of sequences that are not zigzag sequences are 1, 17, 29, 17, 1 and 1, 9, 9.

# ref: http://www.cs.ucf.edu/~dmarino/progcontests/modules/bit/Zigzag2.pdf
def findZigZagSequence(a, n):
    a.sort()
    mid = int((n + 1)/2 - 1)
    a[mid], a[n-1] = a[n-1], a[mid]

    st = mid + 1
    ed = n - 2
    while st <= ed:
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed - 1

    for i in range (n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end = ' ')
    return

print(findZigZagSequence([2,3,5,1,4], 5))