#  match is a part of HorizonPair
#  HorizonPair is free software: you can redistribute it and/or modify it under the terms of the gnu general public license as published by the free software foundation, either version 3 of the license, or (at your option) any later version.
#
#  HorizonPair is distributed in the hope that it will be useful, but without any warranty; without even the implied warranty of merchantability or fitness for a particular purpose. see the gnu general public license for more details.
#
#  you should have received a copy of the gnu general public license along with HorizonPair. if not, see <https://www.gnu.org/licenses/>.


from horizonpair.chess.player import Player
from horizonpair.chess.result import Result


class Match:
    """A chess match."""

    def __init__(
        self, white_player: Player = None, black_player: Player = None, round=0
    ) -> None:
        self.white_player = white_player
        self.black_player = black_player
        self.round = round
        self.over = False
        self.result: Result = None

    def __str__(self) -> str:
        return f"""--- match begin ---
Match in round: {self.round}
Is it over? { self.over }
result: { self.result }
White: { self.white_player }
    ---
Black: { self.black_player }
--- match end ---
"""

    def conclude(result: Result) -> None:
        """Signal that the Match has concluded, and result is the Result"""
        self.over = True
        self.result = result


if __name__ == "__main__":
    m = Match(white_player="XXX", black_player="XXX")
    print(m)
