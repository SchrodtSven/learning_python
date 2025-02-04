# FILE: built-in/while.py 
# SUBJECT: while learning Python: 
#
# AUTHOR: Sven Schrodt <sven@schrodt.club>
# SINCE:  2025-01-02
import time
i = 1
while i < 6:
  print(i)
  time.sleep(0.8)
  i += 1
else:
  print("i is no longer less than 6")
  
  user_inp = ''
  secret = 'stop'
  while user_inp.lower() != secret:
    user_inp = input('your choice!')

