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

    def __repr__(self) -> str:
        """a more detailed representation of the match"""
        return f"""--- match begin ---
Match in round: {self.round}
Is it over? { self.over }
result: { self.result }
White: { self.white_player }
    ---
Black: { self.black_player }
--- match end ---
"""

    def __str__(self) -> str:
        """a short str representation of the match"""
        return f"{self.white_player.name} vs. {self.black_player.name}: result {self.result}"

    def conclude(self, result: Result) -> None:
        """Signal that the Match has concluded, and result is the Result"""
        self.over = True
        self.result = result

    def get_winner(self) -> Player:
        """Get the winner of the match"""
        if self.result == Result.WHITE_WON:
            return self.white_player
        elif self.result == Result.BLACK_WON:
            return self.black_player
        else:
            return None

    def get_result(self) -> Result:
        """Get the result of the match if over. Otherwise None"""
        if self.over:
            return self.result
        else:
            return None


if __name__ == "__main__":
    m = Match(white_player="XXX", black_player="XXX")
    print(m)
