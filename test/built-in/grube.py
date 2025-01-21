# https://docs.python.org/3/library/string.html


my_tuple = (3, 2, 2, 3, 4,99) # tuples are immutable
my_list = [1, 2, 3, 4]

print('{} example: {}', type(my_list), my_list)
print('{} example: {}', type(my_tuple), my_tuple)
print(my_tuple.count(2))

my_list.append(99)

my_list.extend((99,33,1))
my_list.remove()
my_list.sort()
print(my_list)