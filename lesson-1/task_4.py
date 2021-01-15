user_number = int(input('Input an integer number: '))
max_value = 0
value = user_number
increment = 10

while value // 10 != 0:
    value = value % 10
    if value > max_value:
        max_value = value
    value = user_number // increment
    increment *= 10

print(f'In number {user_number} max number value'
      f' is {max_value}')
