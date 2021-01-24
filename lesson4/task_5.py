from functools import reduce

generated_list = [i for i in range(100, 1001, 2)]

print(reduce(lambda arg_1, arg_2: arg_1 * arg_2, generated_list))
