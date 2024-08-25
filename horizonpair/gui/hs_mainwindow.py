#  main_window is part of HorizonSwiss
#  HorizonSwiss is free software: you can redistribute it and/or modify it under the terms of the gnu general public license as published by the free software foundation, either version 3 of the license, or (at your option) any later version.
#
#  HorizonSwiss is distributed in the hope that it will be useful, but without any warranty; without even the implied warranty of merchantability or fitness for a particular purpose. see the gnu general public license for more details.
#
#  you should have received a copy of the gnu general public license along with HorizonSwiss. if not, see <https://www.gnu.org/licenses/>.

from time import sleep
from tkinter import *
from tkinter import ttk

from horizonswiss.chess.colour import Colour
from horizonswiss.chess.match import Match
from horizonswiss.chess.player import Player
from horizonswiss.chess.result import Result
from horizonswiss.gui.widget import MatchWidget, PlayerWidget, RosterWidget
from horizonswiss.test.widget_display_test import WidgetTest
from horizonswiss.tournament import Tournament
from horizonswiss.tournament.round import Round


class WelcomeWindow(ttk.Frame):
    """The visual GUI"""

    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.grid()
        # frame config
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self["borderwidth"] = 12
        self["padding"] = 50  # internal padding inside the frame
        # WIDGETS
        ttk.Label(self, text="HorizonSwiss", font=("tkCaptionFont", 24)).grid(
            row=0, column=0
        )

        self.new_tournament = ttk.Button(
            self, text="New Tournament", command=self.new_tournament
        ).grid(row=1, column=0)

        self.add_player = ttk.Button(
            self, text="Add Player", command=self.add_player
        ).grid(row=2, column=0)

        self.view_players = ttk.Button(
            self, text="View Players", command=self.view_players
        ).grid(row=3, column=0)

    def new_tournament(self):
        """Create a new tournament"""
        # TODO: ADD UI TO CREATE A NEW TOURNAMENT
        showWidgets = WidgetTest(self)
        showWidgets.tkraise()

    def add_player(self):
        """Add a player to the HorizonSwiss system"""
        # TODO: ADD UI TO ADD A PLAYER
        raise NotImplementedError

    def view_players(self):
        """View the players in the HorizonSwiss system"""
        # TODO: ADD UI TO VIEW THE PLAYERS
        raise NotImplementedError


def main() -> None:
    root = Tk()
    root.title("HorizonSwiss")
    welcome_win = WelcomeWindow(root)

    root.mainloop()


if __name__ == "__main__":
    main()
