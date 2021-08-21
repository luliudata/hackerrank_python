def miniMaxSum(arr: list):
    # Write your code here
    sorted_arr_asc = sorted(arr)
    sorted_arr_des = sorted(arr, reverse=True)

    mini_sum = sorted_arr_asc[0] + sorted_arr_asc[1] + sorted_arr_asc[2] + sorted_arr_asc[3]
    max_sum = sorted_arr_des[0] + sorted_arr_des[1] + sorted_arr_des[2] + sorted_arr_des[3]

    print(f"{mini_sum} {max_sum}")



miniMaxSum([1,3,5,7,9])
# sorted_arr_asc = sorted([1,3,5,7,9])
# print(sorted_arr_asc)
