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