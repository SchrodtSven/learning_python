import json
# Sven_MD.json
fh = open('mini.json', 'r')
dta = fh.read()

parsed = json.loads(dta)

for item  in parsed:
    print(item['first_name'])