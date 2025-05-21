import tkinter as tk
from core.file import File
from core.gui import Gui

class Application:
    root = None
    
    def __init__(self, ctxt):
       self.root = ctxt
       print(__name__ + ' started')
       self.file = File()
       self.gui = Gui()
            
    
    def run(self):
        return self.root  
    
    def draw_main_men(self):
        main_mnu = tk.Menu(self.root)
        self.root.config(menu=main_mnu)
        
        ex_data = {
            'Open': self.file.open,
            'Save': self.file.save,
            'Save As': self.file.save_as,
            'spacer': True,
            'Exit': self.root.destroy
        }
        
        sub_mnu = self.gui.sub_mnu('File', ex_data, main_mnu)
        
        
        
    def foo(self):
        print(__name__)
        
        #   find  ~/projects/learning_python/ -type f -name '*.py' -exec grep -n 'ntsc' {} ';'