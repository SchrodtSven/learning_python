# dotd.py | numpy01.py
#
# AUTHOR: Sven Schrodt
# SINCE: 2025-02-19

import numpy as np

# Creating Array of Booleans, depending on found/not found 

def find_name(arr, name):
    return np.where(arr == name, True, False)

def find_name_afoot(arr, name):
    return [True if x == name else False for x in arr]

names = np.array(["Alexandre", "Bob", "Clementine", "Dorothy", "Emile", "Frank", "Gisèle", "Norm"])

frasheers = ['Annie', 'Bebe', 'Bob', 'Cliff', 'Daphne', 'Diane', 'Duke', 'Eddie', 'Frasier','Gil', 'Lana', 'Lilith', 'Martin', 'Dr. Mary', 'Meris', 'Niles','Noel', 'Norm', 'Roz', 'Sam', 'Zora']
# for name in frasheers: 
#     print(list(find_name(names, name)))
#     print(find_name_afoot(names, name))
#     print()

## Reshaping arrays 

redim = names.reshape(4, 2)


print(redim)

print(len(frasheers))
print(np.array(frasheers).reshape(7,3))