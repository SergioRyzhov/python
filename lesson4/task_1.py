from sys import argv

file_name, hours_quantity, hour_rate, bonus_money = argv


def employee_salary(hours, rate, bonus):
    print((int(hours) * int(rate)) + int(bonus))


employee_salary(hours_quantity, hour_rate, bonus_money)
