## FILE: shop/item.py 
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

print(inst._Item__priv)

pass 