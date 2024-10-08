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
from horizonpair.gui.widget import MatchWidget, PlayerWidget, RosterWidget
from horizonpair.tournament import Roster


class WidgetTest(ttk.Frame):
    """The visual GUI"""

    def __init__(self, parent):
        super().__init__(parent, width=500, height=500, padding="3 3 12 12")
        self.grid()

        Label(self, text="match").grid(row=0, column=0)
        # define the match shown
        match = Match(Player("nicolas vaagen", "176141"), Player("rob bin ", "276141"))
        MatchWidget(self, match).grid(row=1, column=0)

        Label(self, text="roster").grid(row=0, column=1)
        # define the roster shown
        roster = Roster(
            [
                Player("nicolas vaagen", "176141"),
                Player("rob bin ", "276141"),
                Player("haduaas vaagen", "676767"),
                Player("root zen", "4233=1"),
                Player("nicosad vaagen", "32=372"),
                Player("Luke Sandwitch", "276141"),
                Player("taytaas swiftn", "345487"),
                Player("no you", "276141"),
                Player("Santa Claus", "5525325"),
                Player("johno canobi ", "321325"),
            ]
        )
        RosterWidget(self, roster).grid(row=1, column=1)

        Label(self, text="player").grid(row=0, column=2)
        # define the player shown
        player = Player("nicolas vaagen", "176141")
        PlayerWidget(self, player).grid(row=1, column=2)


def test() -> None:
    root = Tk()
    root.title("HorizonPair")
    myapp = WidgetTest(root)

    root.mainloop()


if __name__ == "__main__":
    test()
