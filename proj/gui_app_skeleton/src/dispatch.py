class Dispatcher(object):

    def __init__(self, caller, name):
        self.name = name
        self.caller = caller

    def __call__(self, *a, **ka):
        print('Call on Dispatcher registered!', 
              'Will create method on',
              self.caller.__class__.__name__,
              'now.')
        
        print(self.caller, __class__, __name__)
        setattr(self.caller, self.name, self.mock)
        return getattr(self.caller, self.name)(*a, **ka)

    @classmethod
    def mock(cls, *a, **ka):
        print(a,ka, cls)
        return 'Some default value for newly created methods.'


class MyClass(object):

    def __getattr__(self, attr):
        return Dispatcher(self, attr)



instance = MyClass()
#print(instance.new_method, '\n')
#print(instance.new_method(), '\n')
print(instance.foo(23), '\n')
#print(instance.other_method)