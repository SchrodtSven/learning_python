import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import filedialog as fd

filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )

def foo():
    name = username.get()
    messagebox.showinfo(title='General Info', message='You entered: {} - {}'.format(str(name), str(password)))
    file = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)
    messagebox.showinfo(title='General Info', message='You entered:' + file)

# root window
root = tk.Tk()
root.geometry('400x300')
root.title('TTK Demo')

# s = ttk.Style()
# print(s.theme_use())
# exit()

# UI options
paddings = {'padx': 2, 'pady': 2}
entry_font = {'font': ('Chicago', 12)}

username = tk.StringVar()
password = tk.StringVar()


username_label = ttk.Label(root, text="Username:")
username_label.grid(column=0, row=0, sticky=tk.W, **paddings)
username_entry = ttk.Entry(root, textvariable=username, **entry_font)
username_entry.grid(column=1, row=0, sticky=tk.E, **paddings)

# password
password_label = ttk.Label(root, text="Password:").grid(column=0, row=1, sticky=tk.W, **paddings)
password_entry = ttk.Entry(root, textvariable=password, show="*", **entry_font).grid(column=1, row=1, sticky=tk.E, **paddings)
        
        
button = ttk.Button(root, text=' ok ', command=foo).grid(column=1, row=6)


root.mainloop()