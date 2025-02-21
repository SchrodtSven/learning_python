# FILE: transport.py 
#
# SUBJECT: vehicle zoo
#
# AUTHOR: Sven Schrodt <sven@schrodt.club>
# SINCE:  2025-02-045
from time import sleep
from datetime import datetime
class TransportationVehicle:
    
    _speed = None
    
    _brakes = []
    
    _max_speed = 200
    
    def __init__(self, speed = 0):
        self._speed = speed
    
    @property
    def speed(self):
        return self._speed 
    
    @speed.setter
    def speed(self, value: int = 0):
        self._speed = value
        
    def inc_speed(self, value: int):
        self._speed += value
        if self.speed > self._max_speed:
            self.speed = self._max_speed
    
    def dec_speed(self, value: int):
        self._speed -= value
        if self.speed < 0:
            self.full_brake()
        
        
    def full_brake(self):
        self.dec_speed(self.speed)
        self._brakes.append(datetime.now())
        
class Ship(TransportationVehicle):
    
    def toot(self):
        sound = 'Pfoooh!'
        for i in range(len(sound)):
            print(sound[i], sep='')
            sleep(0.3)
            
        print('..')
        
        
foo = TransportationVehicle(123)
print(foo)
print(type(foo))
exit(234)
print(foo.speed)
foo.inc_speed(122)
print(foo.speed)
foo.full_brake()
print(foo.speed)
foo.inc_speed(100)
print(foo.speed)
foo.full_brake()
print(foo._brakes)


my_boat = Ship()
my_boat.toot()
my_boat.inc_speed(55)
print(my_boat.speed)
my_boat.dec_speed(100)
my_boat.inc_speed(500)
print(my_boat.speed)