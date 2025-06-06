import tkinter as tk
from tkinter import ttk

# root window
root = tk.Tk()
root.geometry('400x300')
root.title('Notebook Demo')

# tk.Label(root, text='Classic Label', bg='#232323', fg='white').pack()

ttk.Style().configure("TButton", padding=6, relief="flat", background="#ccc")
ttk.Label(root, text='Themed Label', style="BW.TLabel").pack()
# create a notebook
notebook = ttk.Notebook(root)
notebook.pack(pady=10, expand=True)

# create frames
frame1 = tk.Frame(notebook, width=400, height=280, bg='blue')
frame2 = tk.Frame(notebook, width=400, height=280, bg='orange')
frame3 = tk.Frame(notebook, width=400, height=280, bg='darkgray')



frame1.pack(fill='both', expand=True)
frame2.pack(fill='both', expand=True)

# add frames to notebook

notebook.add(frame1, text='General Information')
notebook.add(frame2, text='Profile')
notebook.add(frame3, text='Foo')
root.mainloop()