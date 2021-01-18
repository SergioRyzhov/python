goods_number = int(input('Input the quantity of goods for the data: '))
goods_list = []
good_dict = {}
stat_list = ['название', 'цена', 'количество', 'eд']

for i in range(goods_number):
    for k in stat_list:
        good_dict.update({k: input(f'Input the "{k}" of the good {i + 1}: ')})
    good_tuple = (i + 1, good_dict.copy())
    goods_list.append(good_tuple)

good_dict_analytics = {}
items_list_analytics = []

for i in range(len(stat_list)):
    for k in range(len(goods_list)):
        try:
            items_list_analytics.append(int(goods_list[k][1][stat_list[i]]))
        except ValueError:
            items_list_analytics.append(goods_list[k][1][stat_list[i]])
    good_dict_analytics.update({stat_list[i]: items_list_analytics.copy()})
    items_list_analytics.clear()

print(good_dict_analytics)
