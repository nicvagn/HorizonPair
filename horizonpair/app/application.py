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

from horizonpair.chess import Colour, Match, Player, Result
from horizonpair.gui import CreateTournamentFrame, ViewTournamentFrame, WelcomeFrame
from horizonpair.gui.widget import (
    MatchWidget,
    PlayerWidget,
    RosterWidget,
    TournamentWidget,
)
from horizonpair.tournament import Roster, Round, Tournament
from horizonpair.tournament.pairing_systems import PairingSystem, Random


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
        menubar.add_command(label="Home", command=self.home)

        self.config(menu=menubar)

        # copy of the shown frame
        self.current_frame = WelcomeFrame(self)

    def clear(self):
        """Clear the window"""
        self.current_frame.destroy()

    def show_frame(self, frame_class: ttk.Frame):
        """Show a frame
        Args:
            frame_class: the frame class to show, can be any subclass of ttk.Frame
        """
        self.clear()
        self.current_frame = frame_class(self)
        self.current_frame.grid(row=0, column=0, sticky=(N, S, E, W))

    def home(self):
        """Go to the home frame"""
        self.clear()
        self.current_frame = WelcomeFrame(self)

    def create_tournament(self):
        """Create a new tournament"""
        self.clear()
        # display the create tournament frame
        self.current_frame = CreateTournamentFrame(self)

    def view_tournament(self):
        """View a tournament"""
        # TODO: ADD ABILITY TO CHOOSE A TOURNAMENT TO VIEW
        self.clear()

        # TODO: THIS IS TEST
        number_of_rounds = 4
        pairing_system = Random()
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

        self.tournament_frame = ViewTournamentFrame(self, self.tournament)
        # show the tournament frame
        self.show_frame(self.tournament_frame)


def start() -> None:
    """Start the application"""
    root = App()

    root.mainloop()


if __name__ == "__main__":
    main()
