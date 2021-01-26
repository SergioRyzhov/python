subject_dict = {}

with open('task_6.txt', 'r', encoding='utf-8') as f:
    for i in f:
        tmp = i.split()
        tmp2 = i.split(':')
        summary = 0
        for k in tmp:
            if k.split('(').pop(0).isdigit():
                summary += int(k.split('(').pop(0))
        subject_dict[tmp2.pop(0)] = summary
print(subject_dict)
