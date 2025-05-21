# FILE: built-in/seq.py 
# SUBJECT: Sequences in Python 
#
# A sequence is a data structure arranging _items_ (diff. values) in an order.
# Any item is accessible by an integer called index, that represents its 
# position (in the sequence).
# Every sequence has a length/size -> SEE: len()
#
# AUTHOR: Sven Schrodt <sven@schrodt.club>
# SINCE:  2025-01-17 
# 

# Tuples  
# - immutable
my_tuple = (1, 2, 4, 8)
for i in reversed(my_tuple):
    print(i, end=' ')
print()
# A list is a list is ...


my_list = ['France', 'Austria', 'Belgium']

print(len(my_list)) # 3
print(my_list.count('Austria')) # 1
print(my_list.count('Germany')) # 0
print(my_list[2]) # 'Belgium'  -> index start at 0

#  - mutable 
my_list.append('Germany') # Adding new item to list
print(my_list.count('Germany')) # 1 

# - accessible via index 
my_list[3] = 'Italy' # Overwriting 'Germany'
my_list.append('Spain')

print(my_list)


# will result in TypeError: list assignment index out of range
try: 
    # my_list[9] = 'Italy'
    my_list['Foo'] = 'Italy'
except TypeError as ie:
    print(ie)

# you can mix types in a list 
my_list.append(23)
print(my_list)

# even lists are possible items in a list - nested list example: 
print(['a', 'b', ['cc', 'dd', ['eee', 'fff']], 'g', 'h'])

# An index can also contain a range - called: slice - start:end containing item with idx start and NOT containing item at position end

# - accessible via slice (in index syntax)
print(my_list[1:3]) # ['Austria', 'Belgium']


## List Comprehension

## List comprehension is a way to create lists using a concise syntax allowing
## the creation of a new list by applying an expression to each item of an 
## interable object (list, range, ...) TODO: check others


## original list
numbers = [1, 2, 3, 99]

## list comprehensions to create new list
doubled_numbers = [num * 2 for num in numbers]
squares = [num * num for num in numbers]

## list comprehension vs. for loop

a = [1, 2, 3, 4, 5]
# Create an empty list 'res' to store results
res = []
# Iterate over each element in list 'a'
for val in a:
      # Multiply each element by 2 and append it to 'res'
    res.append(val * 2)
print(res)

# list comprehension in one line
res = [val * 2 for val in [1, 2, 3, 4, 5]]
print(res)

# list comprehension calling function

dates = [
    "01.10.2024", "02.10.2024", "03.10.2024", "04.10.2024", "05.10.2024",
    "06.10.2024", "07.10.2024", "08.10.2024", "09.10.2024", "10.10.2024",
    "11.10.2024", "12.10.2024", "13.10.2024", "14.10.2024", "15.10.2024",
    "16.10.2024", "17.10.2024", "18.10.2024", "19.10.2024", "20.10.2024",
    "21.10.2024"
]

def date_de_iso(date1):
    day, month, year = date1.split('.')
    return '-'.join([year, month, day])

print(date_de_iso(dates[3]))

iso_dates = [date_de_iso(i) for i in dates]
print(iso_dates)




# list concatenation

concatted_list = [3, 2, 2] + [99, 102, 1]
concatted_list.sort()
my_sum = sum(concatted_list)
print(f'Sum of {concatted_list} is {my_sum}')
print(concatted_list)

fruits = ['apple', 'pear', 'orange', 'banana', 'garden strawberry', 'pear']
# insert at postion -> shift others to the right hand 
fruits.insert(0, 'kiwi')
# append to the end of a list
fruits.append('gooseberry')
fruits.sort()

for i in range(len(fruits)):
    print(fruits[i])
i_dont_like = 'pear'

removed = 0
while fruits.count(i_dont_like) != 0:
    # remove 1st element with given value    
    fruits.remove(i_dont_like)
    removed +=1
    
print('Python removed {} items with value "{}"'.format(removed, i_dont_like))
# delete item at index 0 -> shift others to the left
del(fruits[0])
print(fruits)



