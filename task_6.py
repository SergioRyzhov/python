begin_distance = float(input('Input begin distance, km: '))
aim_distance = float(input('Input aim distance, km: '))
count_days = 1

while begin_distance < aim_distance:
    begin_distance = begin_distance * 0.1 + begin_distance
    count_days += 1
print(f'Your result will be achieved in {count_days} days')
