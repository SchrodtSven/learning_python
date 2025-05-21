import tkinter as tk

class Gui:
    """ Class helping building parts of GUIs from data structures """
    
    def sub_mnu(self, name, data, main_mnu):
        
        
        
        sub_mnu = tk.Menu(main_mnu)
        main_mnu.add_cascade(label=name, menu=sub_mnu)
        for item in data:
            if item == 'spacer':
                sub_mnu.add_separator()
            else:
                sub_mnu.add_command(label=item, command=data[item])
    
        return sub_mnu