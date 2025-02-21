from  __future__ import barry_as_FLUFL as flufl

for attr in dir(flufl):
    print(attr)
    if callable(attr):
        print(f'{attr} is callable')
        
print(callable(print))
        