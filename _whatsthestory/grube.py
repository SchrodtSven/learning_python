# FILE: _whatsthestory/property_story.py 
#
# SUBJECT: Eplaining the Python @property decorator 
#
# AUTHOR: Sven Schrodt <sven@schrodt.club>
# SINCE:  2025-02-04
# SEE:  https://www.programiz.com/python-programming/decorator


# In Python, a decorator is a design pattern that allows you to modify the 
# functionality of a function by wrapping it in another function.
# The outer function is called the decorator, which takes the original 
# function as an argument and returns a modified version of it.


def harmless_greeting(name):
    def inner_circle():
        return "Non serviam, " + name + "!"
    return inner_circle

greet = harmless_greeting("Hagbard")
print(greet())  # prints


def smart_divide(func):
    def inner(a, b):
        print("I am going to divide", a, "and", b)
        if b == 0:
            print("Whoops! cannot divide")
            return

        return func(a, b)
    return inner

@smart_divide
def divide(a, b):
    print(a/b)

divide(2,5)

divide(2,0)