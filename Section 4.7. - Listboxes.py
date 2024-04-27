import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry('600x400')
root.resizable(False, False)
root.title('Listboxes')

programming_languages = ('C', 'Go', 'JS', 'Perl', 'Python', 'Rust')
langs = tk.StringVar(value=programming_languages)
langs_selected = tk.Listbox(
    root,
    listvariable=langs, #we use listvariable and not stringvariable because 'programming_languages' is tuple
    height=6,
    selectmode='extended', #to be able to select multiple elements (the opposite is 'browse')
)
langs_selected.pack()


def handle_selection_change(event):
    selected_indices = langs_selected.curselection()
    for i in selected_indices:
        print(langs_selected.get(i))

langs_selected.bind('<<ListboxSelect>>', handle_selection_change)
root.mainloop()