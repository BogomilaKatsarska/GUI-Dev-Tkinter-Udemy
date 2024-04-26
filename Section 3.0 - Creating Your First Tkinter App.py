'''
tkinter._test() - test whether Tkinter has been installed
entries == text field with info from user
'''
import tkinter as tk
from tkinter import ttk


def greet():
    print(f'Hello, {user_name.get() or "World"}!')

#root is the main window
root = tk.Tk()

user_name = tk.StringVar()

#entry field
name_label = ttk.Label(
    root,
    text='Name: ',
)
name_label.pack(
    side='left',
    padx=(0, 10),
)
name_entry = ttk.Entry(
    root,
    width=15, # not in px, but in number of chars that the field should be able to accommodate
    textvariable=user_name,
)
name_entry.pack(side='left')
name_entry.focus() #.focus() so we can start typing as we open the app

greet_button = ttk.Button(
    root,
    text='Greet',
    command=greet,
)
greet_button.pack(
    side='left', #default value of side is 'top'
    fill='y', #fill 'y' - to fill up the entire reserved space
    expand=True, #the button grows together with the window
)

quit_button = ttk.Button(
    root,
    text='Quit',
    command=root.destroy, #root.destroy destroys the window
)
quit_button.pack()

#to the label we must pass the parent - i.e. root
#pack puts the element into the window
ttk.Label(
    root,
    text='Hello, World!',
    padding=(30, 10),
).pack()

#pause Python code temporarily
root.mainloop()
