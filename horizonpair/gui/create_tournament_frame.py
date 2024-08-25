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
        # WIDGETS
        ttk.Label(self, text="Name:").grid(row=0, column=0)
        name_entry = ttk.Entry(self).grid(row=0, column=1)

        ttk.Label(self, text="pairing system:").grid(row=1, column=0)
        swiss_system = ttk.Radiobutton(self, text="swiss").grid(row=1, column=1)
        random_system = ttk.Radiobutton(self, text="random").grid(row=1, column=2)

        ttk.Label(self, text="Number of rounds:").grid(row=3, column=0)
        num_rounds_entry = ttk.Spinbox(self, from_=1, to=20).grid(row=3, column=1)

        ttk.Label(self, text="Acceleration method:").grid(row=4, column=0)
        no_acceleration = ttk.Radiobutton(self, text="no acceleration").grid(
            row=4, column=1
        )

        self.add_player = ttk.Button(
            self, text="Add Player", command=self.add_player
        ).grid(row=8, column=2)

        self.new_tournament = ttk.Button(self, text="Submit", command=self.submit).grid(
            row=8, column=3
        )

    def add_player(self):
        """Add a player to the Tournament"""
        # TODO: this

        raise NotImplementedError

    def submit(self):
        """Create the tournament"""
        # TODO: ADD UI TO CREATE A NEW TOURNAMENT

        self.created_tournament = Tournament(
            name="HorizonPair",
            roster=Roster(),
            pairing_system=Random(),
            number_of_rounds=4,
            acceleration_method="no acceleration",
        )

    def add_player(self):
        """Add a player to the HorizonPair system"""
        # TODO: ADD UI TO ADD A PLAYER
        raise NotImplementedError


def main() -> None:
    raise NotImplementedError
    root.mainloop()


if __name__ == "__main__":
    main()
