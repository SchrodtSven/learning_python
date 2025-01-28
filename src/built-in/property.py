class C:
    def __init__(self):
        self._x = None

    @property
    def x(self):
        """I'm the 'x' property."""
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x
        
my_c = C()
my_c.foo ='LOrem Ipsum'

my_c.x = 'lalal'

print(getattr(my_c, 'x'))

my_c.x = 'Lirum larum'
print(my_c.x)
print(getattr(my_c, 'x'))

 