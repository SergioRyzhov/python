data_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

new_data_list = [i for i in data_list if data_list.count(i) == 1]

print(new_data_list)
