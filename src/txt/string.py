

class String(str):
    def quote(self, sign="'"):
        return(sign + self + sign)
    
    def __add__(self, other):
        return super.__add__(self, other)
    
s = String('lorem ipsum')
t = s+s
print(type(t))
print(t.quote())