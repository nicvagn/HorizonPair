#  match_widget is part of HorizonPair
#  HorizonPair is free software: you can redistribute it and/or modify it under the terms of the gnu general public license as published by the free software foundation, either version 3 of the license, or (at your option) any later version.
#
#  HorizonPair is distributed in the hope that it will be useful, but without any warranty; without even the implied warranty of merchantability or fitness for a particular purpose. see the gnu general public license for more details.
#
#  you should have received a copy of the gnu general public license along with HorizonPair. if not, see <https://www.gnu.org/licenses/>.

from tkinter import *
from tkinter import ttk

import horizonpair.gui.styles
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


class MatchWidget(ttk.Frame):
    """The visual rep. of a game. Black and white player, round, etc."""

    def __init__(self, parent, match: Match):
        super().__init__(parent, width=500, height=500, padding="3 3 12 12")

        self.grid(column=0, row=0, sticky=(N, W, E, S))
        # White Player
        ttk.Label(self, text=f"White: { match.white_player }", style="WB.TLabel").grid(
            column=1, row=1, padx=3, pady=3
        )

        # Black Player
        ttk.Label(self, text=f"Black: { match.black_player }", style="BW.TLabel").grid(
            column=2, row=1, padx=3, pady=3
        )


def test() -> None:
    root = tk()
    root.title("match widget")

    # define the match shown
    match = Match(player("nicolas vaagen", "176141"), player("rob bin ", "276141"))
    widget = matchwidget(root, match)

    # print_hierarchy(widget)
    root.mainloop()


if __name__ == "__main__":
    test()
