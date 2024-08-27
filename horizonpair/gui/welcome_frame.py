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


class WelcomeFrame(ttk.Frame):
    """The welcome frame for the GUI"""

    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.parent = parent
        self.grid(sticky=(N, S, E, W))
        # frame config
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self["borderwidth"] = 12
        self["padding"] = 50  # internal padding inside the frame
        # WIDGETS
        ttk.Label(self, text="HorizonPair", font=("tkCaptionFont", 24)).grid(
            row=0, column=0, sticky=(N, E, W)
        )

        self.create_tournament_btn = ttk.Button(
            self, text="New Tournament", command=self.create_tournament
        ).grid(row=1, column=0, sticky=(N, E, W))

        self.view_tournament_btn = ttk.Button(
            self, text="View Tournament", command=parent.view_tournament
        ).grid(row=2, column=0, sticky=(N, E, W))

        self.add_player_btn = ttk.Button(
            self, text="Add Player", command=self.add_player
        ).grid(row=3, column=0, sticky=(N, E, W))

        self.view_players_btn = ttk.Button(
            self, text="View Players", command=self.view_players
        ).grid(row=4, column=0, sticky=(N, E, W))

    def create_tournament(self):
        """Create a new tournament"""
        # TODO: ADD UI TO CREATE A NEW TOURNAMENT

        self.parent.create_tournament()

    def add_player(self):
        """Add a player to the HorizonPair system"""
        # TODO: ADD UI TO ADD A PLAYER
        raise NotImplementedError

    def view_players(self):
        """View the players in the HorizonPair system"""
        # TODO: ADD UI TO VIEW THE PLAYERS
        raise NotImplementedError


def main() -> None:
    raise NotImplementedError


if __name__ == "__main__":
    main()
