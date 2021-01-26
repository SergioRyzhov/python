import json

frm_dict = {}
avg_prft_dict = {}

with open('task_7.txt', 'r', encoding='utf-8') as f:
    profit = 0
    count = 0
    for i in f:
        tmp = i.split()
        frm_dict[tmp[0]] = int(tmp[2]) \
                           - int(tmp[3].split('.').pop(0))
        if int(tmp[3].split('.').pop(0)) < int(tmp[2]):
            count += 1
            profit += frm_dict[tmp[0]]
            avg_prft_dict['average_profit'] = int(profit / count)

data_list = [frm_dict, avg_prft_dict]

with open('task_7.json', 'w') as fj:
    json.dump(data_list, fj)
