#  tournament_widget is part of HorizonPair
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
from horizonpair.gui.widget import PlayerWidget, RosterWidget
from horizonpair.tournament import Tournament
from horizonpair.tournament.roster import Roster
from horizonpair.tournament.round import Round


class TournamentWidget(ttk.LabelFrame):
    """A visual reperesentation of a chess roster."""

    def __init__(self, parent, tournament: Tournament) -> None:
        """arguments:
        parent[ttk.Widget] -- The parent widget in the hierarchy
        roster[tournament] -- The Tournament this widget is displaying
        """
        super().__init__(parent, width=500, height=500, padding="3 3 12 12")

        self.grid(column=0, row=0, sticky=(N, W, E, S))

        self.name_label = ttk.Label(self, text=tournament.get_name())
        self.name_label.grid(column=0, row=0, sticky=(N, W, E, S))

        self.roster_widget = RosterWidget(self, tournament.get_roster())

        self.roster_widget.grid(column=0, row=1, sticky=(N, W, E, S))


# testing
if __name__ == "__main__":
    root = Tk()
    root.geometry("600x600")
    roster = Roster(
        [
            Player("player 1", "cfc id 1"),
            Player("player 2", "cfc id 2"),
            Player("player 3", "cfc id 3"),
        ]
    )
    RosterWidget(root, roster).pack()
    root.mainloop()
