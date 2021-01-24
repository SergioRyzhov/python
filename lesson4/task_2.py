data_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

new_data_list = [data_list[i] for i in range(1, len(data_list))
                 if data_list[i] > (data_list[i - 1])]

print(data_list)
print(new_data_list)
