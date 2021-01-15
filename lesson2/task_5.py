user_rate_number = int(input('Input the rate number: '))
my_list = [7, 5, 3, 3, 2]
my_list2 = my_list.copy()
trigger = True

for i in range(len(my_list)):
    if user_rate_number > my_list[i]:
        my_list2.insert(i, user_rate_number)
        trigger = False
        break

if trigger:
    my_list2.reverse()
    for i in range(len(my_list)):
        if user_rate_number <= my_list2[i]:
            my_list2.insert(i, user_rate_number)
            break
    my_list2.reverse()

print(my_list2)
