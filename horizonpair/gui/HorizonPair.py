#  HorizonPair is free software: you can redistribute it and/or modify it under the terms of the gnu general public license as published by the free software foundation, either version 3 of the license, or (at your option) any later version.
#
#  HorizonPair is distributed in the hope that it will be useful, but without any warranty; without even the implied warranty of merchantability or fitness for a particular purpose. see the gnu general public license for more details.
#
#  you should have received a copy of the gnu general public license along with HorizonPair. if not, see <https://www.gnu.org/licenses/>.

import tkinter as tk
from time import sleep
from tkinter import ttk

from chess.colour import Colour
from chess.match import Match
from chess.player import Player
from chess.result import Result
from tournament import Tournament
from tournament.round import Round


class App(ttk.Frame):
    """The visual GUI"""

    def __init__(self, parent):
        super().__init__(parent, width=500, height=500, padding="3 3 12 12")
        self.grid()

        ttk.Label(self, text="Hello, world").grid()


def main() -> None:
    root = tk.Tk()
    root.title("HorizonPair")
    myapp = App(root)

    root.mainloop()


def main_() -> None:
    pass


if __name__ == "__main__":
    main_()
