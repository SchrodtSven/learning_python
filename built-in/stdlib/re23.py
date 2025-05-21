import re
# pattern = r'\b[A-Z]{.*}\b'

pattern = r'[^.]\s([A-Z][a-z]\w+)'
txt = 'meine kleine SAmmlung an Ballonseidee'

print(re.findall(pattern, txt))