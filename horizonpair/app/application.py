#  __main__.py is part of HorizonPair
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
from horizonpair.gui.create_tournament_frame import CreateTournamentFrame
from horizonpair.gui.welcome_frame import WelcomeFrame
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


class App(Tk):
    """The root application"""

    def __init__(self):
        super().__init__()
        self.title("HorizonPair")
        # No tearoff menus
        self.option_add("*tearOff", False)

        menubar = Menu(self)
        menu_file = Menu(menubar)
        menu_edit = Menu(menubar)
        menubar.add_cascade(menu=menu_file, label="Load")
        menubar.add_cascade(menu=menu_edit, label="IDK")

        self.config(menu=menubar)

        # copy of the shown frame
        self.current_frame = WelcomeFrame(self)

    def clear(self):
        """Clear the window"""
        self.current_frame.destroy()

    def create_tournament(self):
        """Create a new tournament"""
        self.clear()
        self.current_frame = CreateTournamentFrame(self)

    def view_tournament(self):
        """View a tournament"""
        # TODO: ADD ABILITY TO CHOOSE A TOURNAMENT TO VIEW
        self.clear()

        # TODO: THIS IS TEST
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
        self.tournament = Tournament(
            name="Test Tournament",
            roster=rotster,
            pairing_system=pairing_system,
            number_of_rounds=number_of_rounds,
        )

        self.tournament_frame = TournamentWidget(self.current_frame, self.tournament)
        self.tournament_frame.grid(column=0, row=0, sticky=(N, W, E, S))


def start() -> None:
    """Start the application"""
    root = App()

    root.mainloop()


if __name__ == "__main__":
    main()
