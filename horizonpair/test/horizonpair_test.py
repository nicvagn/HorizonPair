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
