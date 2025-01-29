# FILE: whatsnew_in/python_3.0.py 
# 
# SUBJECT: New in Python 3.0
#
# AUTHOR: Sven Schrodt <sven@schrodt.club>
# SINCE:  2025-01-28
# 

# Hint: Since i am starting with Python 3.13 I will not get deep into Python 2.* stuff
# The print statement has been replaced with a print() function, with keyword
# arguments to replace most of the special syntax of the old print statement 
# (SEE: PEP 3105). 
# 
# Examples:
# Old: print "The answer is", 2*2

print("The answer is", str(2*2) +'2' ) # New

print("The end is near", end=" ") # space not newline
print() # printing newline

print(3/2)
print(3//2)

# dict.items() returning views (NOT lists)
foo = {"name": "Sven", "age": "yes"}
print(foo.keys())
print(type(foo.items()))
print(foo.values())

