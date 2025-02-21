# FILE: welcome.py 
#
# SUBJECT: Hello world generator
#
# AUTHOR: Sven Schrodt <sven@schrodt.club>
# SINCE:  2025-02-05

class welcome:
    _my_dict = []
    _secret = 0xd0
    _sentence = None
    _parts_prefix = '0x'
    _glue = '@'
    
    def __init__(self):
        print(self._secret)
        
    def encrypt_me(self, sentence: str) ->str:
        self.my_dict = [hex(ord(char) + self._secret) for char in sentence]
        self._sentence = self._glue.join(self._my_dict)
        return self._sentence
        # for char in sentence:
        #     self._my_dict.append(hex(ord(char) + self._secret))
        #     self._sentence = self._glue.join(self._my_dict)
        # return self._sentence
    
    def decrypt_me(self, cryp_txt: str)-> list:
        tmp = [chr(int(char.replace(self._parts_prefix, ''), 16) - self._secret) for char in cryp_txt.split(self._glue)]
        return ''.join(tmp)
        
    @property 
    def my_dict(self):
        return self._my_dict
    
    @my_dict.setter
    def my_dict(self, value: str):
        self._my_dict = value
    
    
    
    
                 
orig = 'Jean-Pierres Welt'
a = welcome()
a.encrypt_me(orig)
 
print(a.my_dict)
print(a._sentence)

txt = a.decrypt_me(a._sentence)
print(txt)

assert(orig  == txt)


    
