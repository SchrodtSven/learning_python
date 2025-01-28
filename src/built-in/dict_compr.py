# FILE: built-in/dict_compr.py
# SUBJECT: Dict Comprehension in Python 
#
# AUTHOR: Sven Schrodt <sven@schrodt.club>
# SINCE: 2025-01-27


# Linking two lists (conditionally with if/else) as keys(names) and values (duties) of a generated dict
names = ['Anna', 'Benjamin', 'Clara', 'Doerthy', 'Uncle $crooge', 'Hermann', 'Helga']
duties = ['Baking pretzels', 'Beer brewing', 'Kraut preparing', 'Weizenbier drinking', 'Telling bad jokes', 'being nice', 'Karaoke']


idyll_dict_wipe = {names[i]: 'Wiping road' if names[i] in ('Benjamin', 'Helga') else duties[i] for i in range(len(names)) }

print(idyll_dict_wipe)



