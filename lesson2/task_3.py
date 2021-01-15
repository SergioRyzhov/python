while True:
    month_number = int(input('Input natural number of the Month: '))
    if 13 > month_number > 0:
        break
    else:
        print('You should input a number between 1 and 12!')

year_time = ['winter', 'spring', 'summer', 'autumn']

year_time_dict = {
    1: 'winter',
    2: 'spring',
    3: 'summer',
    4: 'autumn'
}

if 2 < month_number < 6:
    print(f'By list: {year_time[1]}')
    print(f'By dict: {year_time_dict[2]}')
elif 5 < month_number < 9:
    print(f'By list: {year_time[2]}')
    print(f'By dict: {year_time_dict[3]}')
elif 8 < month_number < 12:
    print(f'By list: {year_time[3]}')
    print(f'By dict: {year_time_dict[4]}')
else:
    print(f'By list: {year_time[0]}')
    print(f'By dict: {year_time_dict[1]}')
