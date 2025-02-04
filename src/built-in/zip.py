# FILE: built-in/zip.py
# SUBJECT: zip, zip hooray...
#
# AUTHOR: Sven Schrodt <sven@schrodt.club>
# SINCE: 2025-01-28

languages = ['Java', 'Python', 'JavaScript', 'Rust', 'PHP', 'Perl']
versions = [14, 3.13, 6, 1.84, 8.4, 5.34]
result = zip(languages, versions)

print(list(result))

first_name = ['Piggy','Earl','Theresa','Martina','Dougie', 'Stan']
hobby = ['Walking','Boxing','Fishing','Bowling','Hacking','CNCing']
born = [1923, 1965, 2011, 2006, 1983,1904]

for f, h, b in zip(first_name, hobby, born):
     print(f"{f} with hobby '{h}' was born in {b} ")
    
print(list(zip(born, first_name, hobby)))
    