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

from horizonpair.cfc import CfcId
from horizonpair.chess.colour import Colour


class Player:
    """A chess player in a tournament."""

    def __init__(self, name: str, cfc_id: CfcId) -> None:
        self.name: str = name
        self.cfc_id: CfcId = cfc_id

        # history of the matches this player has been in. Empty to start.
        self.match_history = list()

    def __str__(self) -> str:
        return f"""Player with name: { self.name }
CFC ID: { self.cfc_id }
match history: { self.match_history }\n"""

    def __repr__(self) -> str:
        return self.__str__()

    def __lt__(self, other) -> bool:
        return self.name < other.name

    def colour_preferance(self) -> Colour:
        raise NotImplementedError
