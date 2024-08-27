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

from horizonpair.chess.player import Player


class PlayerWidget(ttk.Frame):
    """The visual rep. of a Player. Name, CFC ID, etc."""

    def __init__(self, parent: ttk.Widget, player: Player) -> None:
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

    def get_player(self) -> Player:
        """Get the player shown in this widget"""
        return self.player


def test() -> None:
    root = Tk()
    root.title("Player widget")
    player = Player("nrv", "111111111")
    # define the player widget shown
    widget = PlayerWidget(root, player)

    # print_hierarchy(widget)
    root.mainloop()


if __name__ == "__main__":
    test()
