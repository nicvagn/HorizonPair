#  HorizonPair is free software: you can redistribute it and/or modify it under the terms of the gnu general public license as published by the free software foundation, either version 3 of the license, or (at your option) any later version.
#
#  HorizonPair is distributed in the hope that it will be useful, but without any warranty; without even the implied warranty of merchantability or fitness for a particular purpose. see the gnu general public license for more details.
#
#  you should have received a copy of the gnu general public license along with HorizonPair. if not, see <https://www.gnu.org/licenses/>.

from time import sleep
from tkinter import *
from tkinter import ttk

from horizonpair.chess.colour import Colour
from horizonpair.chess.match import Match
from horizonpair.chess.player import Player
from horizonpair.chess.result import Result
from horizonpair.gui.widget import MatchWidget
from horizonpair.tournament import Tournament
from horizonpair.tournament.round import Round


class App(ttk.Frame):
    """The visual GUI"""

    def __init__(self, parent):
        super().__init__(parent, width=500, height=500, padding="3 3 12 12")
        self.grid()

        # define the match shown
        match = Match(Player("nicolas vaagen", "176141"), Player("rob bin ", "276141"))
        MatchWidget(self, match)


def main() -> None:
    root = Tk()
    root.title("HorizonPair")
    myapp = App(root)

    root.mainloop()


if __name__ == "__main__":
    main()
