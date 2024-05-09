import tkinter as tk
from tkinter import ttk

root = tk.Tk()
style = ttk.Style(root)

#inherit from default styles
style.configure('CustomEntryStyle.TEntry', padding=20)

name = ttk.Label(root, text='Hello, world!')
entry = ttk.Entry(root, width=15)
entry['style'] = 'CustomEntryStyle.TEntry'
name.pack()
entry.pack()

entry2 = ttk.Entry(root, width=15)
entry2.pack()

root.mainloop()