# dict.py

x = {'name': 'Sven', 'Profession': 'H@kk3R'}
y = {'Born': '1970-12-09', 'Location': 'Finistère'}
z = {**x, **y, **{'foo': 'Bar'}} # remember: * is for postional, ** for named arguments
print(z)

#exit(224)




# Using dict to remove duplicates from a list, the Pytonic way
my_tuple = ('key1', 'key2', 'key3', 'key1')

# init with given keys an value 12
my_dict = dict.fromkeys(my_tuple, 12)
print(my_dict)

for k in my_dict:
    print(k, ':', my_dict[k])
    print('{}: {}'.format(k, my_dict[k]))
# convert to list from dict keys    
my_list = list(my_dict.keys())
print(my_list)





f =range(26)
for i in f:
    print(chr(i+65), end=' ')
    
#### dict comprehension 


namen = ['Anna', 'Benjamin', 'Clara', 'David', 'Onkel Hubert', 'Eva', 'Hans']
aufgaben = ['Brezeln backen', 'Bier bringen', 'Kraut zubereiten', 
            'Weißwürste besorgen', 'schlechte Witze erzählen', 'brav sein', 
            'Beim Karaoke schief mitsingen']
idyll_dict_wipe = {namen[i]: 'Auffahrt fegen' if namen[i] in ('Hans', 'Onkel Hubert') else aufgaben[i] for i in range(len(namen)) }
print(idyll_dict_wipe)