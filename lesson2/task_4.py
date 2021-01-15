user_string = input('Input some space separated string: ')

for ind, i in enumerate(user_string.split()):
    print(ind, i[:10])
