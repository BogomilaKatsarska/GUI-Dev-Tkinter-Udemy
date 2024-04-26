import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry('600x400')
root.resizable(False, False)
root.title('Widget Examples')

text = tk.Text(
    root,
    height=8, #8rows of text
)
text.pack()
text.insert('1.0', 'Please enter a comment...') # 1.0 is the position at which you want to insert your text - 1st line, 0th char
text['state'] = 'disabled' # disable field, 'normal' is the opposite

text_content = text.get('1.0', 'end')
root.mainloop()