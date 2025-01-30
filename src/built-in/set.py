# FILE: built-in/set.py 
# 
# SUBJECT: Using sets in Python
#
# AUTHOR: Sven Schrodt <sven@schrodt.club>
# SINCE:  2025-01-30
# 

# What is a set - definition:
#   - Sets are unordered.
#   - Set elements are unique. Duplicate elements are not allowed.
#   - A set itself may be modified, but the elements contained in the set must
# be of an immutable type.

# Usage:
# A: set(<iterable)
#       |........ iterable     ...........|
x = set(['foo', 'bar', 'baz', 'foo', 'qux'])

s = 'quux'
sl = list(s)
ss = set(s)

# B: Alternately, a set can be defined with curly braces ({}):
# x = {<obj>, <obj>, ..., <obj>}

x = {'foo', 'bar', 'baz', 'foo', 'qux'}

# set comprehension: A compact way to process all or part of the elements in 
# an iterable and return a set with the results. results = {c for c in 
# 'abracadabra' if c not in 'abc'} generates the set of strings {'r', 'd'}. 

results = {c for c in 'abracadabra' if c not in 'abc'}

# To create an empty set you have to use the function set(), because {} 
# creates an empty dict

# Because lists and dictionaries are mutable, they can’t be set as elements
# of a set:

# >>> a = [1, 2, 3]
# >>> {a}
# Traceback (most recent call last):
#   File "<python-input-10>", line 1, in <module>
#     {a}
# TypeError: unhashable type: 'list'

# Operating on a set
# Operators vs. Methods

# Most, though not quite all, set operations in Python can be performed in two
# different ways: by operator or by method. Let’s take a look at how these 
# operators and methods work, using set union as an example.

# Union of the snake - not @ 'seven an the ragged tiger' side-B, but in Python
# x1.union(x2[, x3 ...]) OR
# x1 | x2 [| x3 ...]
# Given two sets, x1 and x2, the union of x1 and x2 is a set consisting of all
# elements in either set.

# Consider these two sets:

x1 = {'foo', 'bar', 'baz'}
x2 = {'baz', 'qux', 'quux'}

# The *union* of x1 and x2 is {'foo', 'bar', 'baz', 'qux', 'quux'}.
# Note: Notice that the element 'baz', which appears in both x1 and x2, 
# appears only once in the union. Sets never contain duplicate values.

# In Python, set union can be performed with the | operator:

x1 = {'foo', 'bar', 'baz'}
x2 = {'baz', 'qux', 'quux'}
x3 = x1 | x2
print(x3)
# {'baz', 'quux', 'qux', 'bar', 'foo'}

# Set union can also be obtained with the .union() method. The method is 
# invoked on one of the sets, and the other is passed as an argument:

x3 = x1.union(x2)
{'baz', 'quux', 'qux', 'bar', 'foo'}
print(x3)