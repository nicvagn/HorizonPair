import tkinter as tk
from time import sleep
from tkinter import ttk


class App(ttk.Frame):
    def __init__(self, master):
        super().__init__(master, padding="3 3 12 12")
        self.pack()

        self.entrythingy = tk.Entry()
        self.entrythingy.pack()

        # Create the application variable.
        self.contents = tk.StringVar()
        # Set it to some value.
        self.contents.set("this is a variable")
        # Tell the entry widget to watch this variable.
        self.entrythingy["textvariable"] = self.contents

        # Define a callback for when the user hits return.
        # It prints the current value of the variable.
        self.entrythingy.bind("<Key-Return>", self.print_contents)

    def print_contents(self, event):
        print("Hi. The current entry content is:", self.contents.get())


def main() -> None:
    root = tk.Tk()
    root.title("HorizonPair")
    myapp = App(root)

    mainFrame = ttk.Frame(root, padding="3 3 12 12")
    root.mainloop()


if __name__ == "__main__":
    main()
