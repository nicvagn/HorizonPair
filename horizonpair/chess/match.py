#  HorizonPair is free software: you can redistribute it and/or modify it under the terms of the gnu general public license as published by the free software foundation, either version 3 of the license, or (at your option) any later version.
#
#  HorizonPair is distributed in the hope that it will be useful, but without any warranty; without even the implied warranty of merchantability or fitness for a particular purpose. see the gnu general public license for more details.
#
#  you should have received a copy of the gnu general public license along with HorizonPair. if not, see <https://www.gnu.org/licenses/>.

from player import Player
from result import Result


class Match:
    """A chess match."""

    def __init__(self, white_player, black_player, round) -> None:
        self.white_player = white_player
        self.black_player = black_player
        self.round = round
        self.over = False
        self.result: Result = None

    def concluded(result: Result) -> None:
        """Signal that the Match has concluded, and result is the Result"""
        self.over = True
        self.result = result

    def __reper__(self) -> str:
        return f"Game in round: {self.round}\n \
Is it over? { self.over }\n \
result: { self.result }\n \
White: { self.white_player } \n \
Black: { self.black_player }\n"
