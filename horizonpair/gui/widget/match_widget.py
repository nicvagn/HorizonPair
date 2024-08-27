#    HorizonPair: a program for assisting in creating and running chess tournaments
#    Copyright (C) 2024 Nicolas Vaagen
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
from tkinter import *
from tkinter import ttk

from horizonpair.chess.colour import Colour
from horizonpair.chess.match import Match
from horizonpair.chess.player import Player
from horizonpair.chess.result import Result
from horizonpair.tournament.round import Round
from horizonpair.tournament.tournament import Tournament


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
        super().__init__(parent, padding="3 3 12 12")

        self.grid(column=0, row=0, sticky=(N, W, E, S))
        # White Player
        ttk.Label(self, text=f"White: { match.white_player }", style="WB.TLabel").grid(
            column=1, row=1, padx=3, pady=3
        )

        # Black Player
        ttk.Label(self, text=f"Black: { match.black_player }", style="BW.TLabel").grid(
            column=2, row=1, padx=3, pady=3
        )

    def get_match(self) -> Match:
        """Get the match shown in this widget"""
        return self.match


def test() -> None:
    root = Tk()
    root.title("match widget")

    # define the match shown
    match = Match(Player("nicolas vaagen", "176141"), Player("rob bin ", "276141"))
    widget = MatchWidget(root, match)

    # print_hierarchy(widget)
    root.mainloop()


if __name__ == "__main__":
    test()
