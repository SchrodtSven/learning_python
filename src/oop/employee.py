# oop/employee.py - an example class demonstraing Python __descriptors__
#
# SEE: https://realpython.com/python-getter-setter/
#
# AUTHOR: Sven Schrodt <sven@schrodt.club>
# SINCE:  2025-01-23
# 

from datetime import date

class GenericDate:
    def __set_name__(self, owner, name):
        self._name = name
        
    def __get__(self, instance, owner):
        return instance.__dict__[self._name]

    def __set__(self, instance, value):
        instance.__dict__[self._name] = date.fromisoformat(value)

class Employee:
    birth_date = GenericDate()
    start_date = GenericDate()

    def __init__(self, name, birth_date, start_date):
        self.name = name
        self.birth_date = birth_date
        self.start_date = start_date

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value.upper()


Sven = Employee('Sven', '1970-12-09', '2026-01-01')
print(Sven.birth_date)
Sven.birth_location = 'Kamp-Lintfort'
print(Sven.birth_location)