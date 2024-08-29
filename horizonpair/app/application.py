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

from horizonpair.chess import Player
from horizonpair.gui import (
    AddPlayerFrame,
    CreateTournamentFrame,
    ViewTournamentFrame,
    WelcomeFrame,
)
from horizonpair.tournament import Roster, Tournament


class App(Tk):
    """The root application"""

    def __init__(self):
        super().__init__()
        self.title("HorizonPair")
        # No tearoff menus
        self.option_add("*tearOff", False)

        menubar = Menu(self)
        menu_home = Menu(menubar)
        menu_edit = Menu(menubar)
        menubar.add_cascade(menu=menu_home, label="Load")
        menubar.add_command(label="Home", command=self.home)

        self.config(menu=menubar)

        self.root_frame = ttk.Frame(self)

        self.current_frame = None

        # copy of the shown frame, and show welcome frame
        self.show_frame(WelcomeFrame(self))

        # data
        self.players = []
        self.tournaments = []

    def clear(self):
        """Clear the window"""
        if self.current_frame is not None:
            self.current_frame.destroy()

    def show_frame(self, frame: ttk.Frame):
        """Show a frame
        Args:
            frame: the frame to show, can be any subclass of ttk.Frame
        """
        self.clear()
        self.current_frame = frame
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

    def show_add_player_frame(self):
        """Show the add player frame"""

        self.show_frame(AddPlayerFrame(self))

    def add_player(self, player: Player):
        """Add a player to the internal players db"""
        # TODO: ADD A PLAYER TO A PERSISTANT DATABASE

        self.players.append(player)


def start() -> None:
    """Start the application"""
    root = App()

    root.mainloop()


if __name__ == "__main__":
    start()
