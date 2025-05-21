# oop/get_set.py - an example class getters and setters
#
# SEE: https://python-course.eu/oop/properties-vs-getters-and-setters.php
#
# AUTHOR: Sven Schrodt <sven@schrodt.club>
# SINCE:  2025-01-23
# 
class P:

    def __init__(self, x):
        self.__x = x
        print('An instance of {} was created'.format(__name__))

    def get_x(self):
        return self.__x

    def set_x(self, x):
        self.__x = x

mine = P(99)
print(mine.get_x())
mine.foo = 'Sven'

