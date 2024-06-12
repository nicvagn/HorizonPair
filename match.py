"""
This file is a part of Horizon Pair

Horizon Pair is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>. 
"""

from enum import Enum

from Player import Player


class winner(Enum):
    """winner of a chess match"""

    WHITE = auto()
    BLACK = auto()
    DRAW = auto()
    UNDECIDED = auto()


class Match:
    """a chess match, paired by Horizon Pair"""

    def __init__(white: Player, black: Player) -> None:
        self.white: Player = white
        self.black: Player = black
        # no result when a game is created
        self.result: winner = winner.UNDECIDED

    def white_won() -> None:
        """white won the match."""
        self.result = winner.WHITE

    def black_won() -> None:
        """black won the match."""
        self.result = winner.BLACK

    def draw() -> None:
        """game is a draw"""
        self.result = winner.DRAW
