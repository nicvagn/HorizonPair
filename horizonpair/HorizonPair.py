#  HorizonPair is free software: you can redistribute it and/or modify it under the terms of the gnu general public license as published by the free software foundation, either version 3 of the license, or (at your option) any later version.
#
#  HorizonPair is distributed in the hope that it will be useful, but without any warranty; without even the implied warranty of merchantability or fitness for a particular purpose. see the gnu general public license for more details.
#
#  you should have received a copy of the gnu general public license along with HorizonPair. if not, see <https://www.gnu.org/licenses/>.

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
