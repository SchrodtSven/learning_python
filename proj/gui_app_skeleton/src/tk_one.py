import tkinter as tk

root = tk.Tk()
root.title('Cells with entry elements in grid')
root.config(bg="skyblue")
root.state('zoomed')
cells=[]

for x in range (43):
    for y in range(11):
       f =  tk.Entry(root, width=4)
       f.grid(column=x, row=y)       
       f.insert(0, f'{x}/{y}')
       cells.append(f)

root.mainloop()


# (3 / 7)
