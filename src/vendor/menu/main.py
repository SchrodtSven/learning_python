# Main file for menu applications
#  
# SINCE 2025-01-20 iday
# AUTHOR Sven Schrodt <sven@schrodt.club>

import re, collections

class Menu:
    sc_start = '['
    sc_end = ']'
    
    def get_shortcut(self, txt):
        idx_s = txt.find(self.sc_start)
        idx_e= txt.find(self.sc_end)
        
        if idx_s != -1 and idx_e != -1:
            return txt[idx_s + len(self.sc_start):idx_e].lower()
        else:
            # print('Mäh!')
            return None
    def strip_special_chars(self, txt):
        return txt.replace(self.sc_end, '').replace(self.sc_start, '')
  
    def dry_run(self, opt):
        # FIXME - run checks
        return True  
    
    def is_seq(self, opt):
        if isinstance(opt, collections.MutableSequence):
            return True
        else: 
            return False

option = ['[D]atei',
          '[E]dit',
          'De[b]ug',
          '[P]rint]']

menu = Menu()
for i in range(len(option)):
    print(menu.get_shortcut(option[i]), '-', menu.strip_special_chars(option[i]))