from itertools import count, cycle

cycle_list = [True, False, 'd', 5]

for i in count(3):
    if i > 10:
        break
    else:
        print(i)

k = 0
for i in cycle(cycle_list):
    if k < 7:
        print(i)
        k += 1
    else:
        break
