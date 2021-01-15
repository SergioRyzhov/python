element_quantity = int(input('Input quantity of elements for the list: '))
user_list = []

el = 1
while el <= element_quantity:
    user_list.append(input(f'Input {el} element of the list: '))
    el += 1

user_list2 = user_list.copy()

i = 0
for el in range(len(user_list2) // 2):
    user_list2[i], user_list2[i + 1] = user_list2[i + 1], user_list2[i]
    i += 2
    if len(user_list2) % 2 != 0 and i == len(user_list2) - 1:
        break

print(f'User list is:      {user_list}')
print(f'Formatted list is: {user_list2}')
