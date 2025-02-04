# FILE: built-in/numbers.py
# SUBJECT: how to write numbers (/numeric literals) in Python 
#
# AUTHOR: Sven Schrodt <sven@schrodt.club>
# SINCE: 2025-02-04

# underscore groupies arriving...
a = 1_00_00  # you do not need to group digits by three!
b = 1_000_00.0 # nor my the same amount of digits 


hexmex = 0xbad_c0ffee | 0xdead_beef # you can make jokes with hexadecimal digit notation


summ_summ = 0b0101_01010101010_0100  # works with binary notation
busy_bee = 0b01010101
full_bumble = 0b11111111
calculated = ~busy_bee # not binary 
print(calculated, '{0:b}'.format(calculated), ' {0:b}'.format(busy_bee), sep="\n")
# print(a, b, hexmex, summ_summ, full_bumble, busy_bee, sep="\n")
print(bin(255))
print(bin(129))
print(hex(3735928559).upper())
print(0xdead_beef)