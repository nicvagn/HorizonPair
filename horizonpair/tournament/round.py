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
from horizonpair.chess.match import Match
from horizonpair.chess.player import Player


class Round:
    """A round of chess games that are part of a tournament"""

    def __init__(self, round_number: int, matches: [Match]) -> None:
        self.round_number = round_number
        self.matches = matches

    def __str__(self) -> str:
        """Get a str reperesenation of this round."""
        string_rep = f"Round number: { self.round_number }\n"
        if self.matches is None:
            string_rep += "No Matches\n"
        else:
            for m in self.matches:
                string_rep += str(m)

        return string_rep
