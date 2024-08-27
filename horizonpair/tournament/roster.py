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
from horizonpair.chess.match import Match
from horizonpair.chess.player import Player
from horizonpair.chess.result import Result


class Roster:
    """A Roster of players in a chess tournament"""

    def __init__(self, players: list[Player]) -> None:
        """arguments:
        players[list[Player]] -- The list of players in the roster
        """
        # for the basic roster, sort the players py p.__lt__()
        self.player_list = sorted(players)

        self.number_of_players = len(self.player_list)

    def __str__(self) -> str:
        return "\n".join([str(player) for player in self.player_list])

    def __repr__(self) -> str:
        return "\n".join([repr(player) for player in self.player_list])

    def __len__(self) -> int:
        return len(self.player_list)

    def get_playes(self) -> list[Player]:
        """return the list of players in the roster"""
        return self.player_list


def test() -> None:
    player_list = [
        Player("player 1", CfcId("111111")),
        Player("player 2", CfcId("222222")),
        Player("player 3", CfcId("333333")),
        Player("player 4", CfcId("444444")),
    ]
    roster = Roster(player_list)
    print(roster)


if __name__ == "__main__":
    test()
