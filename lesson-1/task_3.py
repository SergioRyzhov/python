user_number = int(input('Input a number: '))
number_string = str(user_number)
number_sum = user_number + int(number_string * 2) + \
             int(number_string * 3)

print(f'{number_string} + {number_string * 2} + '
      f'{number_string * 3} = ', number_sum)
