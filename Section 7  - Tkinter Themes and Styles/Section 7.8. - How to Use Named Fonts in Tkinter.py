import tkinter as tk
from tkinter import ttk
import tkinter.font as font

root = tk.Tk()
style = ttk.Style()
print(font.families())

#Special Family Names: Courier, Times and Helvetica
#Default in Windows is 'System'
WarningLabelFont = font.Font(family='Helvetica', size=14, weight='bold')

'''
Change the size to some of our widgets:

SecondWarningLabelFort = font.nametofont('TkDefaultFont').copy()
SecondWarningLabelFort.configure(size=15)
'''
name = ttk.Label(root, text='Hello, world', font=WarningLabelFont)
entry = ttk.Entry(root, width=15)
button = ttk.Button(root, text='Press me')
name.pack()
entry.pack()
button.pack()

root.mainloop()