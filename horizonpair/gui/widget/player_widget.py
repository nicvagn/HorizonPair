#  match_widget is part of HorizonPair
#  HorizonPair is free software: you can redistribute it and/or modify it under the terms of the gnu general public license as published by the free software foundation, either version 3 of the license, or (at your option) any later version.
#
#  HorizonPair is distributed in the hope that it will be useful, but without any warranty; without even the implied warranty of merchantability or fitness for a particular purpose. see the gnu general public license for more details.
#
#  you should have received a copy of the gnu general public license along with HorizonPair. if not, see <https://www.gnu.org/licenses/>.

from tkinter import *
from tkinter import ttk

import horizonpair.chess.colour
import horizonpair.chess.match
import horizonpair.chess.player
import horizonpair.chess.result
import horizonpair.tournament.round
import horizonpair.tournament.tournament


class PlayerWidget(ttk.Frame):
    """The visual rep. of a Player. Name, CFC ID, etc."""

    def __init__(self, parent: ttk.Widget, player: player.Player) -> None:
        """arguments:
        parent[ttk.Widget] -- The parent widget in the hierarchy
        player[Player] -- The Player this widget is displaying
        """
        super().__init__(parent, padding="3 3 12 12")

        self.grid(column=0, row=0, sticky=(N, W, E, S))
        ttk.Label(self, text=f"Name: { player.name }").grid(
            column=1, row=1, padx=1, pady=1
        )

        ttk.Label(self, text=f"CFC ID: { player.cfc_id }", style="BW.TLabel").grid(
            column=2, row=1, padx=1, pady=1
        )


def test() -> None:
    root = Tk()
    root.title("Player widget")

    # define the player widget shown
    widget = PlayerWidget(root, match)

    # print_hierarchy(widget)
    root.mainloop()


if __name__ == "__main__":
    test()
