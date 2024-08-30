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

from horizonpair.cfc.id import CfcId
from horizonpair.chess import Player


class AddPlayerFrame(ttk.Frame):
    """The add player frame for the GUI. Used to add a player to the database"""

    def __init__(self, parent) -> None:
        """Args:
        parent: the parent tkinter frame
        """
        super().__init__(parent)
        self.parent = parent
        self.grid(sticky=(N, S, E, W))
        # frame config
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self["borderwidth"] = 12
        self["padding"] = 50  # internal padding inside the frame
        # WIDGETS
        ttk.Label(self, text="Add Player", font=("tkCaptionFont", 24)).grid(
            row=0, column=0, sticky=(N, W, E)
        )
        # Name
        ttk.Label(self, text="Name:", font=("tkCaptionFont", 14)).grid(
            row=1, column=0, sticky=(N, W)
        )
        self.player_name = StringVar()
        ttk.Entry(self, textvariable=self.player_name).grid(
            row=1, column=1, sticky=(N, W, E)
        )

        # CFC ID
        ttk.Label(self, text="CFC ID:", font=("tkCaptionFont", 14)).grid(
            row=2, column=0, sticky=(N, W)
        )
        self.cfc_id = StringVar()
        ttk.Entry(self, textvariable=self.cfc_id).grid(
            row=2, column=1, sticky=(N, W, E)
        )

        # add player button
        ttk.Button(
            self,
            text="Add player to HorizonPair database",
            command=self.add_player,
        ).grid(row=3, column=1, sticky=(S, E))

    def add_player(self) -> None:
        """Add the player to the application database"""
        player = Player(name=self.player_name.get(), cfc_id=CfcId(self.cfc_id.get()))
        # add the player to the database, ie pass it up the chain.
        self.parent.add_player(player)
