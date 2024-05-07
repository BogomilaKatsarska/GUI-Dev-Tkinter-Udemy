import tkinter as tk
from tkinter import ttk

root = tk.Tk()
style = ttk.Style(root)

name = ttk.Label(
    root,
    text='Hello World',
)
entry = ttk.Entry(
    root,
    width=15,
)
name.pack()

# print(name['style'])
print(name.winfo_class()) # => modify TLabel class if you want to chane widgets
root.mainloop()