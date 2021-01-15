revenue = float(input("Input the company's revenue: "))
costs = float(input("Input the company's costs: "))

income = revenue / costs

if revenue <= costs:
    print('The company does not earn!')
else:
    print(f'The company earns money! The income is {income}$')
    employee_quantity = int(input('Input the number of company employees: '))

    employee_earn = income / employee_quantity

    print(f'The earn of 1 employ is {employee_earn}$')
