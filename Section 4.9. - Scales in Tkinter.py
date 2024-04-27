import tkinter as tk
from tkinter import ttk
'''
scale - a line of a draggable pil
'''
root = tk.Tk()
root.geometry('600x400')
root.resizable(False, False)
root.title('Scale')

scale = ttk.Scale(
    root,
    orient='horizontal',
    from_=0,
    to=10,
)
scale.pack(fill='x')# to fill up the entire screen

root.mainloop()