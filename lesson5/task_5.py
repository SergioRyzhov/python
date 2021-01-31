import random


def ls_to_int(my_list):
    my_list2 = []
    for i in my_list:
        my_list2.append(int(i))
    return my_list2


with open('task_5.txt', 'w+') as f:
    for i in range(5):
        f.write(str(random.randint(1, 100)) + ' ')
    f.seek(0)
    tmp = sum(ls_to_int(f.read().split()))
print(f'The summ of the elements from task_5.txt is: {tmp}')
