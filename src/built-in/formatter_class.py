# SUBJECT: Using the built-in formatter class

#  The Formatter class has the following public methods:
#  - format(format_string, /, *args, **kwargs)¶
# 
# AUTHOR: Sven Schrodt <sven@schrodt.club>
# SINCE:  2025-01-17 
# 

# Using Python Standard Library math package for 

import math
class Foo:
    
    # particular representation for human consumption, --> SEE: dunder.py
    def __repr__(self):
        return 'Murx'
    
print(f'PI is approx. {math.pi:.5f}.') # rounded to 5 places after decimal
# PI is approx. 3.14159.

print(math.e)

print(repr(Foo))
print(repr(Foo()))

