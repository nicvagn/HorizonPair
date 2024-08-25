#  HorizonPair is free software: you can redistribute it and/or modify it under the terms of the gnu general public license as published by the free software foundation, either version 3 of the license, or (at your option) any later version.
#
#  HorizonPair is distributed in the hope that it will be useful, but without any warranty; without even the implied warranty of merchantability or fitness for a particular purpose. see the gnu general public license for more details.
#
#  you should have received a copy of the gnu general public license along with HorizonPair. if not, see <https://www.gnu.org/licenses/>.
import horizonpair.tournament
from horizonpair.chess import Player
from horizonpair.tournament.pairing_systems import Random


def test() -> bool:
    """Test pairing a tournament using random pairing for given players"""

    p1 = Player("nic", "1337")
    p2 = Player("yella", "69")
    p3 = Player("rando", "this is a number")
    p4 = Player("yup", "3333333333")

    players = [p1, p2, p3, p4]
    print("Pairing these players")
    for n in range(0, len(players)):
        print(players[n])

    # pair the players
    round1 = Random.pair(1, players)

    print("Match List in this round:")
    for m in round1.matches:
        print(m)

    # pair the players for round 2
    round2 = Random.pair(2, round1.matches)

    print("Match List in this round:")
    for m in round2.matches:
        print(m)

    return True


if __name__ == "__main__":
    test()
