def division(arg_1, arg_2):
    try:
        return arg_1 / arg_2
    except ZeroDivisionError:
        return 'You cannot divide by ZERO!'


print(division(int(input('Input the number1: ')), \
               int(input('Input the number2: '))))
