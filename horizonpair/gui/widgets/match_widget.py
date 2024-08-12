#  match_widget is part of HorizonPair
#  HorizonPair is free software: you can redistribute it and/or modify it under the terms of the gnu general public license as published by the free software foundation, either version 3 of the license, or (at your option) any later version.
#
#  HorizonPair is distributed in the hope that it will be useful, but without any warranty; without even the implied warranty of merchantability or fitness for a particular purpose. see the gnu general public license for more details.
#
#  you should have received a copy of the gnu general public license along with HorizonPair. if not, see <https://www.gnu.org/licenses/>.

from tkinter import *
from tkinter import ttk

from horizonpair.chess.colour import Colour
from horizonpair.chess.match import Match
from horizonpair.chess.player import Player
from horizonpair.chess.result import Result
from horizonpair.tournament import Tournament
from horizonpair.tournament.round import Round


def print_hierarchy(w, depth=0):
    """print a windows widget hierachy"""
    print(
        "  " * depth
        + w.winfo_class()
        + " w="
        + str(w.winfo_width())
        + " h="
        + str(w.winfo_height())
        + " x="
        + str(w.winfo_x())
        + " y="
        + str(w.winfo_y())
    )
    for i in w.winfo_children():
        print_hierarchy(i, depth + 1)


class Match_Widget(ttk.Frame):
    """The visual rep. of a game. Black and white player, round, etc."""

    def __init__(self, parent, match: Match):
        super().__init__(parent, width=500, height=500, padding="3 3 12 12")

        # White Player
        white_name = StringVar(self)
        ttk.Label(self, text=f"White: { match.white_player }").grid(column=1, row=1)
        white_name_label = ttk.Label(self, text="White Player")

        # Black Player
        black_name = StringVar(self)
        ttk.Label(self, text=f"Black: { match.black_player }").grid(column=1, row=3)
        black_name_label = ttk.Label(self, text="Black Player")

        white_name.set("Nicolas Vaagen")
        black_name.set("Jont bluet")

        white_name_label["textvariable"] = white_name

        black_name_label["textvariable"] = black_name

        self.grid(column=0, row=0, sticky=(N, W, E, S))
        white_name_label.grid(column=1, row=2)
        black_name_label.grid(column=1, row=4)


def test() -> None:
    root = Tk()
    root.title("HorizonPair")

    # define the match shown
    match = Match(Player("Nicolas Vaagen", "176141"), Player("Rob Bin ", "276141"))
    widget = Match_Widget(root, match)

    print_hierarchy(root)
    root.mainloop()


if __name__ == "__main__":
    test()
