# FILE: built-in/set.py 
# SUBJECT: Sets in Python 
#
# A set is an unordered collection with _no duplicate elements_. Basic uses 
# include membership testing and eliminating duplicate entries. Set objects 
# also support mathematical operations like union, intersection, difference, 
# and symmetric difference.
# Curly braces or the set() function can be used to create sets. 
# 
# Note: to create an _empty set_ you *have to use set()*, not {}; the latter creates an empty dictionary.
# AUTHOR: Sven Schrodt <sven@schrodt.club>
# SINCE:  2025-01-23
# 

unique_letter_set = set('The quick brown fox jumps over the lazy dog.'.lower())
unique_letter_list =list(unique_letter_set)
unique_letter_list.sort()
unique_letter_list.remove(' ')
unique_letter_list.remove('.')

print(unique_letter_list)