list_1 = ['a', 1, 'hi', 'Yerevan', {"one": 1}, 'flowers']
list_2 = []

for i in range(len(list_1)):
    list_2.append(list_1.pop())


print(list_1)
print(list_2)

