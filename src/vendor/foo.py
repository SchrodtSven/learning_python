
class Foo:
    HIGH_FOO = 255
    LOW_FOO = 0 
    
    def __init__(self, foo_name):
        self.foo_name = foo_name
        
    @property    
    def foo_name(self):
        return self.__foo_name
    
    def foo_name(self, foo_name):
        self.__foo_name = foo_name
        
        
        
my_foo = Foo('Gaby Dom')
print(my_foo.foo_name)


for x in range(25):
    print(2**x)