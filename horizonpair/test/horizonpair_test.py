#  HorizonPair is free software: you can redistribute it and/or modify it under the terms of the gnu general public license as published by the free software foundation, either version 3 of the license, or (at your option) any later version.
#
#  HorizonPair is distributed in the hope that it will be useful, but without any warranty; without even the implied warranty of merchantability or fitness for a particular purpose. see the gnu general public license for more details.
#
#  you should have received a copy of the gnu general public license along with HorizonPair. if not, see <https://www.gnu.org/licenses/>.
from horizonpair.chess.colour import Colour
from horizonpair.chess.match import Match
from horizonpair.chess.player import Player
from horizonpair.chess.result import Result
from horizonpair.tournament import Round, Tournament
from horizonpair.tournament.pairing_systems import Random

list_players = [
    Player("lllllllll", "ididididid"),
    Player("ttttttttt", "ididididid"),
    Player("yyyyyyyyy", "ididididid"),
    Player("xxxxxxxxx", "ididididid"),
    Player("ccccccccc", "ididididid"),
    Player("bbbbbbbbb", "ididididid"),
    Player("sssssssss", "ididididid"),
    Player("#########", "ididididid"),
]
t = Tournament(5, Random, list_players, "test tournament")
round = t.pair_round()


def test() -> bool:
    print("An example round")
    print(round)
    print("An example tournament")
    print(t)

    return True


if __name__ == "__main__":
    test()
