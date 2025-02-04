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

my_cart = Cart()