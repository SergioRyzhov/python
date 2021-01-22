def func_sum_max(arg_1, arg_2, arg_3):
    return sum([arg_1, arg_2, arg_3]) - sorted([arg_1, arg_2, arg_3]).pop(0)


print(func_sum_max(8, 3, 7))
