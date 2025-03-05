# FILE: built-in/op.py 
# SUBJECT: Operators in Python 
#
# AUTHOR: Sven Schrodt <sven@schrodt.club>
# SINCE:  2025-01-23

import operator

a = 3
b = 4

c = operator.add(a, b)
print(c)
assert(c == a+b)
## Ternary Operator

# Since 2.5 Pyhthon has a ternary conditional operator (a if condition else b)
# Note that conditionals are an /expression/, _not a statement_. This means you 
# can't use statements such as pass, or assignments with = (or "augmented"
# assignments like +=), within a conditional expression

a = 10
b = 5
C = 3
foo = a if a < b else (b if C < a else C) 
print(a ,b, foo)

