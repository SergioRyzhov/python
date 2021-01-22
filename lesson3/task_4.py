def power_func2(num_x, num_y):
    power_x = num_x
    if num_y != 0:
        for i in range(1, abs(num_y)):
            power_x *= num_x
        power_x = 1 / power_x
    else:
        power_x = 1
    return power_x


power_func1 = lambda num_x, num_y: num_x ** num_y

print(power_func1(3, -3), power_func2(3, -3))
