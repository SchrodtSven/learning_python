## FILE: shop/user.py 
# 
# SUBJECT: User object for example web shop 2025
#
#
# AUTHOR: Sven Schrodt <sven@schrodt.club>
# SINCE:  2025-02-04
# 
import random, datetime

class User:
    
    def __init__(self, first, last, dob, mail):
        self.first = first
        self.last = last
        self.mail = mail
        self.dob = datetime.date.fromisoformat(dob)
        self._id = 'User_'  + last[:3]  + first + str(self.dob.year)

        
        
        
me = User('Sven', 'Schrodt', '1970-12-09', 'sven@schrodt.nrw')
print(me._id)