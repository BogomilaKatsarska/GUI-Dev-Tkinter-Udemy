import tkinter as tk
from tkinter import ttk
import tkinter.font as font
root = tk.Tk()
style = ttk.Style()

font.nametofont('TkDefaultFont').configure(size=15)
font.nametofont('TkTextFont').configure(size=15)

name = ttk.Label(root, text='Hello, word!')
entry = ttk.Entry(root, width=15)
button = ttk.Button(root, text='Press me')
name.pack()
entry.pack()
button.pack()

root.mainloop()