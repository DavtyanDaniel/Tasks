my_list = [11, 12, 4, 6, 1, 66, 98, -4, 8, 100]
minimum = my_list[0]

for i in range(len(my_list)):
    if my_list[i] < minimum:
        minimum = my_list[i]


print(minimum)