import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry('600x400')
root.resizable(False, False)
root.title('Radio Buttons')

storage_var = tk.StringVar()

option_one = tk.Radiobutton(
    root,
    text='Option 1',
    variable=storage_var,
    value='first option',
)
option_two = tk.Radiobutton(
    root,
    text='Option 2',
    variable=storage_var,
    value='second option',
)
option_three = tk.Radiobutton(
    root,
    text='Option 3',
    variable=storage_var,
    value='third option',
)
option_one.pack()
option_two.pack()
option_three.pack()

root.mainloop()