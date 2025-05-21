# FILE: built-in/property.py 
# SUBJECT: Example class demonstrating the usage of properties
#
# AUTHOR: Sven Schrodt <sven@schrodt.club>
# SINCE:  2025-01-29
# SEE: https://peps.python.org/pep-0008/
# SEE: https://realpython.com/python-classes/#special-methods-and-protocols

from datetime import date

class Employee:
    def __init__(self, name, birth_date):
        self.name = name
        self.birth_date = birth_date

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value.upper()

    @property
    def birth_date(self):
        return self._birth_date

    @birth_date.setter
    def birth_date(self, value):
        self._birth_date = date.fromisoformat(value)

 
john = Employee("John", "2001-02-07")
print(john.name, john.birth_date)
john.name = 'John Foo'

print(john.name, john.birth_date)

print(john.__dict__)