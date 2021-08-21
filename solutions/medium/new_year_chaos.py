#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

# first attempt
# note that:  if anyone has bribed more than two people, print Too chaotic
# the same person, not all the bribes
# using 'dict' % 'list' totally compicates things and slows down the code
# abandon this imcompleted solution
# def minimumBribes(q):
#     # Write your code here
#     counter = 0
#     counter_list = []
#     # start from the first element
#     # compare it with the second element
#     for i in range(len(q) - 1):
#         # if the front element is bigger than the element after it
#         # bride back -> counter +1
#         if q[i] > q[i + 1]:
#             q[i], q[i + 1] = q[i + 1], q[i]
#             counter += 1
#             counter_dict = {
#                 'person_index': i,
#                 'num_bribes': counter
#             }
#             counter_list.append(counter_dict)
#             print(counter_list)
#         else:
#             counter += 0
        # print(counter_list)

        # for item in counter_list:
        #     # print(item['num_bribes']) # find the counternumber
        #     if item['num_bribes'] > 2:
        #         return 'Too chaotic'
        #     else:
        #         return counter

# second attempt
# ref: https://stackoverflow.com/questions/38797194/hackerrank-new-year-chaos-code-optimization?rq=1
def minimumBribes(q):
    # Write your code here
    counter = 0

    # start the loop from q[i] - 2 instead of 0
    # Since no one can jump ahead of its original position by more than 2,
    # so any value higher than q[i] can only be till index q[i] -2.
    for i in range(len(q) - 1, -1, -1):
        print(i) # 3,2,1,0
        if q[i] - (i + 1) > 2:
            print(q[i] - (i + 1))
            print('Too chaotic')
            return
        for j in range(max(0, q[i] - 2), i):
            if q[j] > q[i]:
                counter += 1
    print(counter)

# minimumBribes([1,2,3,5,4])
minimumBribes([4,1,2,3])
