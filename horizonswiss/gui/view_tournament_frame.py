#  view_tournament_frame is part of HorizonSwiss
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
from horizonswiss.gui.widget import (
    MatchWidget,
    PlayerWidget,
    RosterWidget,
    TournamentWidget,
)
from horizonswiss.test.widget_display_test import WidgetTest
from horizonswiss.tournament import Roster, Tournament
from horizonswiss.tournament.pairing_systems import PairingSystem, Random
from horizonswiss.tournament.round import Round


class ViewTournamentFrame(ttk.Frame):
    """The View Tournament frame for the GUI"""

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
        ttk.Label(self, text="HorizonSwiss", font=("tkCaptionFont", 24)).grid(
            row=0, column=0
        )


def test() -> None:
    number_of_rounds = 4
    pairing_system = Random
    rotster = Roster(
        [
            Player("player1", "cfc id player1"),
            Player("player2", "cfc id player2"),
            Player("player3", "cfc id player3"),
            Player("player4", "cfc id player4"),
        ]
    )
    name = "Test tournament"

    self.tournament = Tournament(number_of_rounds, pairing_system, rotster, name)

    self.tournament_frame = TournamentWidget(self, self.tournament)
    self.tournament_frame.grid(column=0, row=0, sticky=(N, W, E, S))


if __name__ == "__main__":
    test()
