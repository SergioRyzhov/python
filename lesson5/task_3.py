with open("task_3.txt", "r") as fo:
    summary = []
    q_string = 0
    print('The list of mans who earn < 20000: ')
    for i in fo:
        if float(i.split().pop(1)) < 20000:
            print(i.split().pop(0))
        q_string += 1
        summary.append(float(i.split().pop(1)))
    middle_earn = sum(summary) / q_string

print(f'The middle earn of all employees is: {middle_earn}')
