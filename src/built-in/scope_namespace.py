# FILE: built-in/scope_namespace.py 
# SUBJECT: Namespaces and Scope in Python 
#
# AUTHOR: Sven Schrodt <sven@schrodt.club>
# SINCE:  2025-01-29
# 


### Class Objects

class MyClass:
    """A simple example class"""
    i = 12345 # data attributes 

    def f(self): #method (also an attribute)
        return 'hello world'
    
print(MyClass.__doc__)

class Complex:

    def __init__(self, realpart, imagpart):

        self.r = realpart

        self.i = imagpart


x = Complex(3.0, -4.5)

print(f'{x.r}, {x.i}')

x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2
print(x.counter) # 16
del x.counter

x = MyClass()
print(x.f())