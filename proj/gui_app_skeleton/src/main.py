import tkinter as tk
from app.application import Application

if __name__ == '__main__':
    ctxt = tk.Tk()
    ctxt.title('Example GUI app skeleton')
    ctxt.state('zoomed')
    
    app = Application(ctxt)
    app.draw_main_men()
    
    ctxt.mainloop()
    
    