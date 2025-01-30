# FILE: built-in/stdlib/dt_stuff.py 
# 
# SUBJECT: Using datetime in Python
#
# AUTHOR: Sven Schrodt <sven@schrodt.club>
# SINCE:  2025-01-30
# 
import datetime
print('Welcome @', datetime.datetime.today())
x = datetime.datetime.fromtimestamp(0)
print(x)

mine =  datetime.datetime.strptime('1970.12.9', '%Y.%m.%d')
print(mine)

