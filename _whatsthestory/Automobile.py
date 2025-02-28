# Class Automobile
# 
# Playing with python class and trying to overload operators
# @since 2024-12-23
# @author Sven Schrodt
import Number

class Automobile:

        # constructor 
        def __init__(self, type, power=100):
            self.type = type
            self.power = power

        # magic method for usage in string context
        def __str__(self):
            return f"An automobile of type: {self.type} with power of: {self.power}"
        
        # overload operator +
        def __add__(self, other):
             return round(self.power + other.power,2) 
        
        # overload operator -
        def __sub__(self, other):
             return abs(round(self.power - other.power,2))
        
        

Hugo = Automobile(type='Ford Ka', power=23.5)

Emile = Automobile(type='Ford Fiesta', power=42.23)

print(Hugo)
print(Emile)
print(Hugo + Emile)
print(Hugo - Emile)

foo = Number.Number(7)
print (2**3)

        

