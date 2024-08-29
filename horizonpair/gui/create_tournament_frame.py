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

from tkinter import *
from tkinter import ttk

from horizonpair.tournament import Roster, Tournament


class CreateTournamentFrame(ttk.Frame):
    """The create_tournament frame for the GUI"""

    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.parent = parent
        self.grid(sticky=(N, S, E, W))
        # frame config
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self["borderwidth"] = 12
        self["padding"] = 50  # internal padding inside the frame

        # VARIABLES - needed for widgets
        pairing_system = StringVar()
        # WIDGETS
        ttk.Label(self, text="Name:").grid(row=0, column=0, sticky=(N, E, W))
        name_entry = ttk.Entry(self).grid(row=0, column=1)

        ttk.Label(self, text="pairing system:").grid(row=1, column=0, sticky=(N, E, W))
        swiss_system_rb = ttk.Radiobutton(
            self, text="swiss", variable=pairing_system, value="swiss"
        ).grid(row=1, column=1, sticky=(E, W))
        random_system_rb = ttk.Radiobutton(
            self, text="random", variable=pairing_system, value="random"
        ).grid(row=1, column=2, sticky=(E, W))

        ttk.Label(self, text="Number of rounds:").grid(
            row=3, column=0, sticky=(N, E, W)
        )
        num_rounds_entry_sbx = ttk.Spinbox(self, from_=1, to=20).grid(
            row=3, column=1, sticky=(E, W)
        )

        ttk.Label(self, text="Acceleration method:").grid(
            row=4, column=0, sticky=(N, E, W)
        )
        no_acceleration_btn = ttk.Radiobutton(
            self, text="no acceleration", value="no"
        ).grid(row=4, column=1, sticky=(E, W))

        acceleration_btn = ttk.Radiobutton(
            self, text="acceleration", value="acceleration"
        ).grid(row=4, column=2, sticky=(E, W))

        self.add_player_btn = ttk.Button(
            self, text="Add Player", command=self.add_player
        ).grid(row=8, column=2, sticky=(N, E, W))

        self.new_tournament_btn = ttk.Button(
            self, text="Submit", command=self.submit
        ).grid(row=8, column=3, sticky=(N, E, W))

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
