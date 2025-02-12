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

class Vehicle:
    created = None
    def __init__(self):
         self.created = datetime.datetime.now()
    
class Car(Vehicile):
    
    carts = {}
    customers = {}
    
    fleet_milage = 0
    
    fleet_milage = 0
    
    
    
        
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
