# dict.py

my_tuple = ('key1', 'key2', 'key3', 'key1')


my_dict = dict.fromkeys(my_tuple, 12)
print(my_dict)

for k in my_dict:
    print(k, ':', my_dict[k])
    print('{}: {}'.format(k, my_dict[k]))
    
my_list = list(my_dict.keys())
print(my_list)
    
    
    