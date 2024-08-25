#  roster is a part of HorizonPair
#  HorizonPair is free software: you can redistribute it and/or modify it under the terms of the gnu general public license as published by the free software foundation, either version 3 of the license, or (at your option) any later version.
#
#  HorizonPair is distributed in the hope that it will be useful, but without any warranty; without even the implied warranty of merchantability or fitness for a particular purpose. see the gnu general public license for more details.
#
#  you should have received a copy of the gnu general public license along with HorizonPair. if not, see <https://www.gnu.org/licenses/>.


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
        self.player_list = players
        # for the basic roster, sort the players by name
        self.player_list = sorted(players)

    def __str__(self) -> str:
        return "\n".join([str(player) for player in self.player_list])

    def __repr__(self) -> str:
        return self.__str__()

    def get_playes(self) -> list[Player]:
        """return the list of players in the roster"""
        return self.player_list


def test() -> None:
    player_list = [
        Player("player 1", "cfc id 1"),
        Player("player 2", "cfc id 2"),
        Player("player 3", "cfc id 3"),
        Player("player 4", "cfc id 4"),
    ]
    roster = Roster(player_list)
    print(roster)


if __name__ == "__main__":
    test()
