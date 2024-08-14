#  round is a part of HorizonPair
#  HorizonPair is free software: you can redistribute it and/or modify it under the terms of the gnu general public license as published by the free software foundation, either version 3 of the license, or (at your option) any later version.
#
#  HorizonPair is distributed in the hope that it will be useful, but without any warranty; without even the implied warranty of merchantability or fitness for a particular purpose. see the gnu general public license for more details.
#
#  you should have received a copy of the gnu general public license along with HorizonPair. if not, see <https://www.gnu.org/licenses/>.

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
