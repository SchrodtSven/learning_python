# FILE: geometry/rectangle.py 
# 
# SUBJECT: Calculations with rectangular 
#
# A sequence is a data structure arranging _items_ (diff. values) in an order.
# Any item is accessible by an integer called index, that represents its 
# position (in the sequence).
# Every sequence has a length/size -> SEE: len()
#
# AUTHOR: Sven Schrodt <sven@schrodt.club>
# SINCE:  2025-01-21
# 

class Rectangle:
    """
        Representing geometric figure <rectangle>
    """
    def __init__(self, width=0.0, length=0.0):
        self.width = width
        self.length = length
    
    def area(self):
        return self.width * self.length
    
    # dunder functions 
    
    def __add__(self, other):
        """ 
            Magic method overloading + operator

        Args:
            other (area): Addding area of another geometric figure

        Returns:
            float: sum of areas
        """
        other_area = getattr(other, 'area', None)
        if callable(other_area):
            return self.area() + other.area()
        
class Foo:
    def area(self): 
        return 2.321
    def __add__(self, other):
        return self.area() + other.area()
        
a = Rectangle(3, 4)
b = Rectangle(1, 2)
print(a.area())
print(b.area())

c = Foo()

print(b + c)


print(c + b)

# help(Rectangle)