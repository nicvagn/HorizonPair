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
import tkinter as tk
from tkinter import ttk

from horizonpair.chess import Player
from horizonpair.gui.frame import (
    AddPlayerFrame,
    CreateTournamentFrame,
    SelectTournamentFrame,
    ViewTournamentFrame,
    WelcomeFrame,
)
from horizonpair.tournament import Roster, Tournament


class App(tk.Tk):
    """The root application"""

    def __init__(self):
        super().__init__()
        self.title("HorizonPair")
        # No tearoff menus
        self.option_add("*tearOff", False)

        menubar = tk.Menu(self)
        menu_file = tk.Menu(menubar)
        menubar.add_cascade(menu=menu_file, label="File")
        menu_file.add_cascade(label="New", command=self.create_tournament)
        menu_file.add_cascade(label="Load", command=self.load_tournament)
        menubar.add_command(label="Home", command=self.home)

        self.config(menu=menubar)

        # the root frame of the gui
        self.root_frame = ttk.Frame(self)

        root_frame = self.root_frame
        root_frame.grid(row=0, column=0, sticky="nsew")

        self.current_frame = None

        # copy of the shown frame, and show welcome frame
        self.swap_frame(WelcomeFrame(self))

        # data
        self.players = []
        self.tournaments = []

    def clear(self):
        """Clear the window"""
        if self.current_frame is not None:
            self.current_frame.destroy()

    def swap_frame(self, frame: ttk.Frame):
        """Swap the shown frame in the GUI
        Args:
            frame: the frame to show, can be any subclass of ttk.Frame
        """
        if frame is not None:
            self.clear()
            self.current_frame = frame
            self.current_frame.grid(row=0, column=0, sticky="nsew")

    def home(self):
        """Go to the home frame"""
        self.swap_frame(WelcomeFrame(self))

    def create_tournament(self):
        """Create a new tournament"""
        # display the create tournament frame
        self.swap_frame(CreateTournamentFrame(self))

    def load_tournament(self):
        """Load a tournament from the database. Shows the view tournament frame"""
        self.swap_frame(SelectTournamentFrame(self))

    def view_tournament(self, tournament: Tournament):
        """View a tournament
        Args:
            tournament: the tournament to view
        """
        self.swap_frame(ViewTournamentFrame(self, tournament))

    def show_add_player_frame(self):
        """Show the add player frame"""

        self.swap_frame(AddPlayerFrame(self))

    def add_player(self, player: Player):
        """Add a player to the internal players db
        Args:
            player: the player to add
        """
        # TODO: ADD A PLAYER TO A PERSISTANT DATABASE

        self.players.append(player)


def start() -> None:
    """Start the application"""
    root = App()

    root.mainloop()


if __name__ == "__main__":
    start()
