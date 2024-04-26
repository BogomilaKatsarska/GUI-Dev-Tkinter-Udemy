import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

root = tk.Tk()
root.resizable(False, False)
root.title("Widget Examples")

label = ttk.Label(root, text="Hello, World!", padding=20)
label.config(font=("Segoe UI", 20))  #Change font ony for the curr label - Tuple of font name and font size
label.pack()

image = Image.open("images/test_image.png").resize((64, 64))
photo = ImageTk.PhotoImage(image)
ttk.Label(root, image=photo, padding=5).pack()

# Change an image associated with a label, if necessary:
# label["image"] = photo


# -- Changing the text of a label dynamically --
greeting = tk.StringVar()

label = ttk.Label(root, padding=10)
label["textvariable"] = greeting
greeting.set("Hello, John!")  # This can change during your program and the label will update.
label.pack()


# -- Combining text and images --
text_image = Image.open("images/test_image.png")
text_photo = ImageTk.PhotoImage(text_image)
ttk.Label(root, text="Image with text.", image=text_photo, padding=5, compound="right").pack() #compound - how image and txt interracts

root.mainloop()

