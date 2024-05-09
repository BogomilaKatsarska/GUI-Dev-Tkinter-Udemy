'''
Tkinter relief values: https://www.tutorialspoint.com/python/tk_relief.htm
'''

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
style = ttk.Style(root)

name = ttk.Label(root, text='Hello, world!')
name.pack()

print(style.layout('TLabel'))
print(style.element_options('Label.border')) # ('relief',)
print(style.element_options('Label.padding')) # ('padding', 'relief', 'shiftrelief')
print(style.element_options('Label.label')) # ('compound', 'space', 'text', 'font', 'foreground', 'underline', 'width', 'anchor', 'justify', 'wraplength', 'embossed', 'image', 'stipple', 'background')

# How to configure the relief property for all els
# style.configure('TLabel', relief='')

print(style.lookup('TLabel', 'font'))
print(style.lookup('TLabel', 'foreground'))
print(style.lookup('TLabel', 'compound'))

style.theme_use('clam') #=> allows to put a border around your labels

print(style.layout('TLabel'))
print(style.element_options('Label.border'))
print(style.element_options('Label.padding'))
print(style.element_options('Label.label'))
print(style.lookup('TLabel', 'font'))
print(style.lookup('TLabel', 'foreground'))
print(style.lookup('TLabel', 'compound'))

style.configure('TLabel', bordercolor='#f00')
style.configure('TLabel', borderwidth=20)
style.configure('TLabel', relief='solid')
root.mainloop()