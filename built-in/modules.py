# FILE: built-in/modules.py
# SUBJECT: Tagesaufgabe 2 zu lambda
#
# AUTHOR: Sven Schrodt <sven@schrodt.club>
# SINCE: 2025-01-29

# example module with mathematical functions

def fibonacci(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

print(fibonacci(9))
