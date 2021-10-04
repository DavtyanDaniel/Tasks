a = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
square = []
my_list = []

for i in a:
    if i % 2 == 0:
        my_list.append(i * 3)

    else:
        square.append(i ** 2)

print(square)
print(my_list)
