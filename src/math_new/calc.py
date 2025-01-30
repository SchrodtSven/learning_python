# FILE: math_new/calc.py 
# SUBJECT: Class  for some calculating stuff - rather Physix than Math, but we ignore it for now
#
# AUTHOR: Sven Schrodt <sven@schrodt.club>
# SINCE:  2025-01-30


def celsius_to_fahrenheit(c = 0.0):
    """ °F = °C  x 1.8 + 32 """  
    return c *1.8 +32


def fahrenheit_to_celsius(f =0.0):
    """ °C = [°F - 32] × (5/9) """  
    return (f - 32) * (5 / 9) 
a = 100.0
assert(a == celsius_to_fahrenheit(fahrenheit_to_celsius(a)))



f = 100 
my_c = fahrenheit_to_celsius(f)

my_f = celsius_to_fahrenheit(my_c)

print(f'F: {f} C: (F->C){my_c} F:(C->F){my_f}')
