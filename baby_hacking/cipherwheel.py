# FILE: baby_hacking/cipherwheel.py 
# SUBJECT: simple crypting
#
# AUTHOR: Sven Schrodt <sven@schrodt.club>
# SINCE:  2025-01-23
# SEE: https://forum.selfhtml.org/self/2008/apr/18/wettangebot-verschluesselung-knacken/1235776#m1235776



def get_alpha_chr(number=0):
    """Getting ASCII letter for number (0 ..25)

    Args:
        number (int, optional): Defaults to 0.

    Raises:
        ValueError: if number is out of bound

    Returns:
        _type_: character -> uppercase letter from A to Z
    """
    number = int(number)
    #print(number)
    if number >=0 and number <=25:
        return chr(number + 65)
    else: 
        raise ValueError('Number MUST have value between 0 and 25')

def get_number_plaintext(txt):
    if len(txt) > 1:
        txt = txt[0]
    return ord(txt.upper())-65

# >> 13
# 01234567890123456789012345
# NOPQRSTUVWXYZABCDEFGHIJKLM
def encrypt_shift_by(number, shifter = 13, ):
    number += shifter
    if number > 25:
        number -= 26
    return number

def get_alphabet_nums():
     return [x for x in range(26)]
 
def get_alphabet_chars():
     return [chr(x+65) for x in range(26)]
     
        
print(get_alpha_chr())
print(get_alpha_chr(13))
print(get_alpha_chr(24))



get_number_plaintext('h')
for character in 'zan':
    print(get_number_plaintext(character)) 
    
print(get_alphabet_chars())
crypted = []
for i in range(26):
    si = str(i)
    if i > 9:
        si = si[1]
    print(si, end='')
    crypted.append(chr(65 + encrypt_shift_by(i)))
print()
print(''.join(crypted))
#print(''.join(get_alphabet_chars()))
# 01234567890123456789012345
# ABCDEFGHIJKLMNOPQRSTUVWXYZ

# >> 13
# 01234567890123456789012345
# NOPQRSTUVWXYZABCDEFGHIJKLM

