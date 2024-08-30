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

from tkinter import ttk
from typing import List

from horizonpair.chess import Colour, Match, Player, Result
from horizonpair.gui.widget import (
    MatchWidget,
    PlayerWidget,
    RosterWidget,
    TournamentWidget,
)
from horizonpair.tournament import Roster, Round, Tournament
from horizonpair.tournament.pairing_systems import PairingSystem, Random


class SelectTournamentFrame(ttk.Frame):
    """The View Tournament frame for the GUI"""

    def __init__(self, parent, tournaments: List[Tournament]) -> None:
        """Args:
        parent: the parent tkinter frame
        tournament: the tournament object to display in the frame
        """
        super().__init__(parent)
        self.parent = parent
        self.grid(sticky="nsew")
        # frame config
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self["borderwidth"] = 12
        self["padding"] = 50  # internal padding inside the frame
        # WIDGETS
        ttk.Label(self, text="Available Tournaments:", font=("tkCaptionFont", 24)).grid(
            row=0, column=0, sticky="nsew"
        )

        # display all tournaments we have available
        y = 1  # row index
        for tournament in tournaments:
            ttk.Button(
                self,
                text=f"{tournament.name}",
                command=lambda t=tournament: self.select_tournament(t),
            ).grid(row=y, column=0, sticky="new")
            y += 1

    def select_tournament(self, tournament: Tournament) -> None:
        """select a tournament from the list of available tournaments in the GUI"""
        self.parent.select_tournament(tournament)
