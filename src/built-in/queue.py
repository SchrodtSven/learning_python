# FILE: built-in/queue.py 
# SUBJECT: Queues in Python 
#
# AUTHOR: Sven Schrodt <sven@schrodt.club>
# SINCE:  2025-01-18
# 

from collections import deque
import sys 
foo = deque(['Hans', 'Frans', 'Herbert', 'Gisbert', 'Susanna'])
print(foo)
first = foo.popleft()
second = foo.popleft()
print(first, second, sep=", ")
print(foo)
print(sys.maxsize)