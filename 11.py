# my_string = "one two"
# ls = my_string.split()
# ls = ls[::-1]
# my_string = ' '.join(ls)
# print(my_string)

my_string = "one two"
stack = []
str1 = ''

for w in my_string:
    if w == ' ':
        stack.append(str1)
        str1 = ''
    else:
        str1 += w
stack.append(str1)

stack = stack[::-1]
my_string = ' '.join(stack)
print(my_string)

