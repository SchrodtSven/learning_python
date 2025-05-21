# FILE: built-in/stdlib/cal.py 
# SUBJECT: Calendar functions in in Python 
#
# AUTHOR: Sven Schrodt <sven@schrodt.club>
# SINCE:  2025-01-30

import calendar
# monthrange - Returns weekday of first day of the month and number of days in month, for the specified year and month. calendar.

my_range = calendar.monthrange(2025, 1)
print(my_range) # (calendar.WEDNESDAY, 31)
days_in_month = []
for i in range(calendar.monthrange(2025, 1)[1]):
    days_in_month.append(str(i+1))
print(', '.join(days_in_month)) 
print(calendar.weekheader(4))
