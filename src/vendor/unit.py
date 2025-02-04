# FILE: vendor/unit.py 
# SUBJECT: Classes representing a unit by its name and value
#
# AUTHOR: Sven Schrodt <sven@schrodt.club>
# SINCE:  2025-01-30

class Unit():
    ERR_INCOMPAT_OP = 'Error: incompatible operands'
    
    def __init__(self, value, unit):
        self.value = float(value)
        self.unit = unit
        
    def __str__(self):
        return str(self.value) + ' ' + self.unit
    
    def raw(self):
        return self.value
    
    def __add__(self, other):
        if self.unit != other.unit:
            raise ValueError(self.ERR_INCOMPAT_OP)
            
        
    
    # FIXME: overloading operators incl. check if other.unit == self.unit!

class Euro(Unit):
    """ Class Euro inherits from Unit """
    def __init__(self, value):
        super().__init__(value, '€')
        
pocket_money_per_month_eur = Euro(999.01)
print(pocket_money_per_month_eur.raw())
print(pocket_money_per_month_eur)