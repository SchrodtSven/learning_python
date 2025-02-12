## FILE: shop/car.py 
# 
# SUBJECT: Class for shop objects for template web shop 2025
#
#
# AUTHOR: Sven Schrodt <sven@schrodt.club>
# SINCE:  2025-02-05
# 
import datetime
from user import User
class Car:
    
    carts = {}
    customers = {}
    
    fleet_milage = 0
    
    fleet_milage = 0
    
    
    def __init__(self):
        self.created = datetime.datetime.now()
        
    def add_customer(self, customer):
        if not isinstance(customer, User):
            print('Error: obj is not an instance of User!!!')
        else:
            self.customers[customer.uid] = customer
            
    @classmethod
    def drive(cls, miles: int):
        cls.fleet_milage += miles

mazda = Car()
mazda.drive(230)

audi = Car()

print(audi.fleet_milage)
# FILE: shop/cart.py 
# 
# SUBJECT: Class for Cart objects for template web shop 2025
#
#
# AUTHOR: Sven Schrodt <sven@schrodt.club>
# SINCE:  2025-02-04
# 
import random, datetime, helper

class Cart:
    
    def __init__(self):
        self.created = datetime.datetime.now()
        self._id = 'Cart_' + helper.create_id(str(self.created.year))
        print('created cart with id: ' + self._id)



#foo = random.randrange(2 ** 16)
#print(foo)

my_cart = Cart()## FILE: shop/geometry.py 
# 
# SUBJECT: Classes for gemetrical objects
#
#
# AUTHOR: Sven Schrodt <sven@schrodt.club>
# SINCE:  2025-02-05


#

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def where_is(point):
    match point:
        case Point(x=0, y=0):
            print("Origin")
        case Point(x=0, y=y):
            print(f"Y={y}")
        case Point(x=x, y=0):
            print(f"X={x}")
        case Point():
            print("Somewhere else")
        case _:
            print("Not a point") 
            
p1 = Point(0,3)
where_is(p1)import datetime

def create_id(string, fill_with='0', width=8):
    """ Creates a random id string based on current datetime

    Args:
        string (_type_): _description_
        fill_with (str, optional): _description_. Defaults to '0'.
        width (int, optional): _description_. Defaults to 8.

    Returns:
        _type_: _description_
    """
    now = datetime.datetime.now().timestamp()
    string = string + str(now).replace('.','')
    return f'{string:{fill_with}>{width}}'
    
    
print(create_id('Sven'))
print(create_id('Test'))
print(create_id('64532'))## FILE: shop/item.py 
# 
# SUBJECT: Class for item objects for template web shop 2025
#
#
# AUTHOR: Sven Schrodt <sven@schrodt.club>
# SINCE:  2025-02-04
# 
class Item:
    
    def __init__(self):
        self.foo = 42
        self._hidden = 23
        self.__priv = 2.3
        
    def show_priv_value(self):
        print(self.__priv)
        
inst = Item()
print(inst.foo)
print(inst._hidden)
#inst.show_priv_value()
print(inst.__dict__)

print(inst._Item__priv)## FILE: shop/item.py 
# 
# SUBJECT: Class for shop objects for template web shop 2025
#
#
# AUTHOR: Sven Schrodt <sven@schrodt.club>
# SINCE:  2025-02-04
# 
import datetime
from user import User
class Shop:
    
    carts = {}
    customers = {}
    
    
    def __init__(self):
        self.opened = datetime.datetime.now()
        
    def add_customer(self, customer):
        if not isinstance(customer, User):
            print('Error: obj is not an instance of User!!!')
        else:
            self.customers[customer.uid] = customer

foo = Shop()
print(foo)
print(foo.opened)
me = User('Sven', 'Schrodt', '1970-12-09', 'sven@schrodt.nrw')
foo.add_customer(me)
## FILE: shop/user.py 
# 
# SUBJECT: Class for User object for example web shop 2025:
#          - is used as item of Shop.
#
#
# AUTHOR: Sven Schrodt <sven@schrodt.club>
# SINCE:  2025-02-04
# 
import random, datetime, helper

class User:
    
    def __init__(self, first, last, dob, mail):
        self.first = first
        self.last = last
        self.mail = mail
        self.dob = datetime.date.fromisoformat(dob)
        self.__id = 'User_'  + helper.create_id(self.last[:3])

    @property
    def first(self):
        return self._first

    @first.setter
    def first(self, value):
        self._first = value

    @first.deleter
    def first(self):
        del self._first
        
    @property
    def uid(self):
        return self.__id
    
    @uid.setter
    def uid(self, value):
        self.__id = value
        
    @uid.deleter
    def uid(self):
        del self.__id
        
        
    # Imagine we had a property for each data attribute ....


p = User('Adam', 'Smythe', '1904-05-23', 'A.Smythe@example.org')
# print('The name is:', p.name)
# p.name = 'John'
# del p.name
        
        
        
me = User('Sven', 'Schrodt', '1970-12-09', 'sven@schrodt.nrw')
print(me)

print(me.uid)
properties = dir(me)
for prop in properties:
    if not prop.startswith('__') and prop not in {'first', 'uid'}:
        print(prop, me.__dict__[prop])