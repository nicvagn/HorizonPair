#  create_tournament_frame is part of HorizonPair
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
from horizonpair.gui.widget import (
    MatchWidget,
    PlayerWidget,
    RosterWidget,
    TournamentWidget,
)
from horizonpair.test.widget_display_test import WidgetTest
from horizonpair.tournament import Roster, Tournament
from horizonpair.tournament.pairing_systems import PairingSystem, Random
from horizonpair.tournament.round import Round


class CreateTournamentFrame(ttk.Frame):
    """The create_tournament frame for the GUI"""

    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.parent = parent
        self.grid()
        # frame config
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self["borderwidth"] = 12
        self["padding"] = 50  # internal padding inside the frame

        # VARIABLES - needed for widgets
        pairing_system = StringVar()
        # WIDGETS
        ttk.Label(self, text="Name:").grid(row=0, column=0)
        name_entry = ttk.Entry(self).grid(row=0, column=1)

        ttk.Label(self, text="pairing system:").grid(row=1, column=0)
        swiss_system_rb = ttk.Radiobutton(
            self, text="swiss", variable=pairing_system, value="swiss"
        ).grid(row=1, column=1)
        random_system_rb = ttk.Radiobutton(
            self, text="random", variable=pairing_system, value="random"
        ).grid(row=1, column=2)

        ttk.Label(self, text="Number of rounds:").grid(row=3, column=0)
        num_rounds_entry_btn = ttk.Spinbox(self, from_=1, to=20).grid(row=3, column=1)

        ttk.Label(self, text="Acceleration method:").grid(row=4, column=0)
        no_acceleration_btn = ttk.Radiobutton(
            self, text="no acceleration", value="no"
        ).grid(row=4, column=1)

        self.add_player_btn = ttk.Button(
            self, text="Add Player", command=self.add_player
        ).grid(row=8, column=2)

        self.new_tournament_btn = ttk.Button(
            self, text="Submit", command=self.submit
        ).grid(row=8, column=3)

    def add_player(self):
        """Add a player to the Tournament"""
        # TODO: this

        raise NotImplementedError

    def create_roster(self) -> Roster:
        """Create a roster from entered players in the GUI"""
        # TODO: create a roster object from the players entered by the user
        raise NotImplementedError

    def submit(self) -> Tournament:
        """Create the tournament"""
        # TODO: finish creating tournament and ...
        # create a roster from the entered players
        roster = self.create_roster()

        # create the tournament specified
        created_tournament = Tournament(name="Test Tournament", roster=roster)

        return created_tournament


def main() -> None:
    raise NotImplementedError
    root.mainloop()


if __name__ == "__main__":
    main()
