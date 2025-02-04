## FILE: shop/item.py 
# 
# SUBJECT: Class for shop objects for template web shop 2025
#
#
# AUTHOR: Sven Schrodt <sven@schrodt.club>
# SINCE:  2025-02-04
# 
import datetime
class Shop:
    
    carts = {}
    
    def __init__(self):
        self.opened = datetime.datetime.now()
        

foo = Shop()
print(foo)
print(foo.opened)

