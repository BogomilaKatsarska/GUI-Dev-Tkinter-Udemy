import tkinter as tk
from tkinter import ttk
'''
dropdown or own value
'''
root = tk.Tk()
root.geometry('600x400')
root.resizable(False, False)
root.title('Combobox')

selected_weekday = tk.StringVar()
weekday = ttk.Combobox(
    root,
    textvariable=selected_weekday,
)
weekday['values'] = (
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday',
    'Sunday',
)
weekday['state'] = 'readonly' # if we do not have this - i.e. 'normal', we will be able to write our own option
weekday.pack()


def handle_selection(event):
    print('Today is ', selected_weekday.get())
    print('We will change it to Friday.')
    selected_weekday.set('Friday')
    print(weekday.current())


weekday.bind('<<ComboboxSelected>>', handle_selection)

root.mainloop()