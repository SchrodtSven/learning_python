## FILE: shop/item.py 
# 
# SUBJECT: Class for shop objects for template web shop 2025
#
#
# AUTHOR: Sven Schrodt <sven@schrodt.club>
# SINCE:  2025-02-04
# 
import datetime
from user import User


class Entity:
    created = None
    modified = None

def __new__(cls):
    cls.created = datetime.datetime.now()
    cls.modified = datetime.datetime.now()


Foo = Entity()

print(dir(Foo.created))

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

# foo = Shop()
# print(foo)
# print(foo.opened)
# me = User(Sven, Schrodt, 1970-12-09, sven@schrodt.nrw)
# foo.add_customer(me)

# txt = hello world!
# enc = []
# for i in range(len(txt)):
#     enc.append(ord(txt[i]))
#     print(txt[i])
    
# print(enc)

def hello_world():
    ENC_NUMER = 0b101010
    chars = [0x92, 0x8f, 0x96, 0x96, 0x99, 0x4a, 0xa1, 0x99, 0x9c, 0x96, 0x8e, 0x4b, 0x2659]
    txt = [chr(i-ENC_NUMER) for i in chars]
    return(''.join(txt))

print(hello_world())