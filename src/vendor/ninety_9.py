# FILE: builvendor/ninety_9.py
# SUBJECT: Let's sing 
#
# AUTHOR: Sven Schrodt <sven@schrodt.club>
# SINCE: 2025-02-04
# SEE: http://www.cs.bme.hu/~friedl/alg/knuth_song_complexity.pdf

what_is_greater_than_ninety_nine = 100 
torso = '{} bottle{} of beer' 
suffix = 'on the wall'
for i in range(what_is_greater_than_ninety_nine -1, 1, -1):
    s = 's' if i > 1 else ''
    print(torso.format(i, s), suffix)
    print(torso.format(i, s))
    
print(100_350)