import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry('600x400')
root.resizable(False, False)
root.title('Spinboxes')

initial_value = tk.IntVar(value=20)
spin_box = tk.Spinbox(
    root,
    from_=0, #if you want to be more concrete, instead of from_ and to, you can use values=(10, 20, 30, 40, 66)
    to=30,
    textvariable=initial_value,
    wrap=False, #if wrap=True, after 30, the value goes back to 0
)
spin_box.pack()

root.mainloop()