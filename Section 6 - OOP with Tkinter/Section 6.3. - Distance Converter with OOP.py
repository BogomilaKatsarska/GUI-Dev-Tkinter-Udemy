'''
'<Return>'      - Special keyword for Enter
'<KP_Enter>'    - Enter for keypad
import tkinter.font as font - fonts
font.nametofont('TkDefaultFont').configure(size=15)
=> does not apply to entries, have to do it manually
winfo_children  - method that allows you to get the children of the widget
== widget info children
'''
import tkinter as tk
import tkinter.font as font
from tkinter import ttk


class DistanceConverter(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title('Distance Converter')

        container = ttk.Frame(self)
        container.grid(padx=60, pady=30, sticky='EW')

        frame = MetresToFeet(container)
        frame.grid(row=0, column=0, sticky='NSEW')

        self.bind('<Return>', frame.calculate_feet)
        self.bind('<KP_Enter>', frame.calculate_feet)


class MetresToFeet(ttk.Frame):
    def __init__(self, container, **kwargs):
        super().__init__(container, **kwargs)

        self.metres_value = tk.StringVar()
        self.feet_value = tk.StringVar()

        metres_label = ttk.Label(self, text='Metres: ')
        metres_input = ttk.Entry(self, width=10, textvariable=self.metres_value, font=('Segoe UI', 15))  # min width
        feet_label = ttk.Label(self, text='Feet: ')
        feet_display = ttk.Label(self, textvariable=self.feet_value)
        calc_button = ttk.Button(self, text='Calculate', command=self.calculate_feet)

        metres_label.grid(column=0, row=0, sticky='W')
        metres_input.grid(column=1, row=0, sticky='EW')
        metres_input.focus()

        feet_label.grid(column=0, row=1, sticky='W')
        feet_display.grid(column=1, row=1, sticky='EW')

        calc_button.grid(column=0, row=2, columnspan=2, sticky='EW')

        for child in self.winfo_children():
            child.grid_configure(padx=15, pady=15)

    def calculate_feet(self, *args):
        try:
            metres = float(self.metres_value.get())
            feet = metres * 3.28084
            self.feet_value.set(f'{feet:.3f}')
        except ValueError:
            pass


class FeetToMetres(ttk.Frame):
    def __init__(self, container, **kwargs):
        super().__init__(container, **kwargs)

        self.metres_value = tk.StringVar()
        self.feet_value = tk.StringVar()

        feet_label = ttk.Label(self, text='Feet: ')
        feet_input = ttk.Entry(self, width=10, textvariable=self.feet_value, font=('Segoe UI', 15))  # min width
        metres_label = ttk.Label(self, text='Metres: ')
        metres_display = ttk.Label(self, textvariable=self.metres_value)
        calc_button = ttk.Button(self, text='Calculate', command=self.calculate_metres)

        feet_label.grid(column=0, row=0, sticky='W')
        feet_input.grid(column=1, row=0, sticky='EW')
        feet_input.focus()

        metres_label.grid(column=0, row=1, sticky='W')
        metres_display.grid(column=1, row=1, sticky='EW')

        calc_button.grid(column=0, row=2, columnspan=2, sticky='EW')

        for child in self.winfo_children():
            child.grid_configure(padx=15, pady=15)

    def calculate_metres(self, *args):
        try:
            feet = float(self.feet_value.get())
            metres = feet / 3.28084
            self.metres_value.set(f'{metres:.3f}')
        except ValueError:
            pass



root = DistanceConverter()

font.nametofont('TkDefaultFont').configure(size=15)

root.columnconfigure(0, weight=1)
root.mainloop()
