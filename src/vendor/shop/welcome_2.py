## FILE: shop/welcome_2.py 
# 
# SUBJECT: hello world variant
#
#
# AUTHOR: Sven Schrodt <sven@schrodt.club>
# SINCE:  2025-02-04
# 

def hello_world():
    ENC_NUMER = 0b101010
  
    chars = [0x92, 0x8f, 0x96, 0x96, 0x99, 0x4a, 0xa1, 0x99, 0x9c, 0x96, 0x8e, 0x4b, 0x2659]
 
    txt = [chr(i-ENC_NUMER) for i in chars]
    return(''.join(txt))

class BeNice:
    numb3rs =  [0x2659, 0x4a, 0x92, 0x8f, 0x96, 0x96, 0x99, 0x4a, 0xa1, 0x99, 0x9c, 0x96, 0x8e, 0x4b]
    make_sense = 4 * 11 -2
    def __init__(self):
        print(''.join([chr(i-self.make_sense) for i in self.numb3rs]))
        
        
        
        
        

#print(hello_world())
BeNice()

s = "ffff"

i=int(s, 16)
print(i)