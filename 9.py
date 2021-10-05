my_list = [-110, -12, -4, -6, -1, -66, -98, -4, -8, -100]
maximum = my_list[0]

for i in range(len(my_list)):
    if my_list[i] > maximum:
        maximum = my_list[i]


print(maximum)

