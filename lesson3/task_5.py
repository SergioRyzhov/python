def add_func(arg):
    result = 0
    for i in arg.split():
        try:
            result = result + int(i)
        except ValueError:
            return result
    return result


print('Input "e" in any position for EXIT')
number_line = input('Input the number line separated by space: ')
summary = 0

while True:
    summary = summary + add_func(number_line)
    print(summary)
    if 'e' in number_line.lower().split():
        break
    number_line = input('Go on input: ')
