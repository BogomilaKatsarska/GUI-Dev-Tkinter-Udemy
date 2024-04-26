import tkinter as tk

root = tk.Tk()
root.geometry('600x400')

rectangle_1 = tk.Label(
    root,
    text='Rectangle 1',
    bg='green',
    fg='white',
)
rectangle_1.pack(
    ipadx=10,
    ipady=10,
    #side='left',
    # fill='both',
    # expand=True,
)

rectangle_2 = tk.Label(
    root,
    text='Rectangle 2',
    bg='red',
    fg='white',
)
rectangle_2.pack(
    ipadx=10,
    ipady=10,
)
root.mainloop()