# FILE: built-in/zip.py
# SUBJECT: zip, zip hooray...
#
# AUTHOR: Sven Schrodt <sven@schrodt.club>
# SINCE: 2025-01-28

languages = ['Java', 'Python', 'JavaScript', 'Rust', 'PHP', 'Perl']
versions = [14, 3.13, 6, 1.84, 8.4, 5.34]
result = zip(languages, versions)

print(list(result))

name = ['Piggy','Earl','Theresa','Madame Quux', 'Martina','Dougie', 'Stan', 'Harlequeen'] 
hobby = ['Walking', 'Hacking', 'Boxing','3D Printing', 'Fishing','Bowling','Nitpicking', 'CNCing']
born = [1923, 1965, 2011, 2001, 2006, 1983, 1904, 1664]

for n, h, b in zip(name, hobby, born):
     print(f"{n} with hobby '{h}' was born in {b} ")
    
#print(list(zip(born, name, hobby)))
