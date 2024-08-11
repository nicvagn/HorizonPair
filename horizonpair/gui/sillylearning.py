from tkinter import *
from tkinter import ttk

root = Tk()

l = ttk.Label(root, text="starting")

l.grid()

l.bind("<Enter>", lambda e: l.configure(text="Inside"))
l.bind("<Leave>", lambda e: l.configure(text="Out!"))

root.mainloop()
