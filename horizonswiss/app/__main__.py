#  __main__.py is part of HorizonSwiss
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
from horizonswiss.gui.welcome_frame import WelcomeFrame
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


class App(Tk):
    """The root application"""

    def __init__(self):
        super().__init__()
        self.title("HorizonSwiss")
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

        raise NotImplementedError

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

        self.tournament = Tournament(number_of_rounds, pairing_system, rotster, name)

        self.tournament_frame = TournamentWidget(self, self.tournament)
        self.tournament_frame.grid(column=0, row=0, sticky=(N, W, E, S))


def main() -> None:
    root = App()

    root.mainloop()


if __name__ == "__main__":
    main()
