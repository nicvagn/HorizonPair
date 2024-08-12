#  HorizonPair is free software: you can redistribute it and/or modify it under the terms of the gnu general public license as published by the free software foundation, either version 3 of the license, or (at your option) any later version.
#
#  HorizonPair is distributed in the hope that it will be useful, but without any warranty; without even the implied warranty of merchantability or fitness for a particular purpose. see the gnu general public license for more details.
#
#  you should have received a copy of the gnu general public license along with HorizonPair. if not, see <https://www.gnu.org/licenses/>.
import horizonpair.tournament
from horizonpair.chess import Player
from horizonpair.tournament.pairing_systems import Random


def test(players: [Player]) -> bool:
    """Test pairing a tournament using random pairing for given players"""

    print("Pairing these players")
    for n in range(0, len(players)):
        print(players[n])

    # pair the players
    match_list = Random.pair(players)

    print("Match List in this round:")
    for m in match_list:
        print("~~~ GAME START ~~~")
        print(m)
        print("~~~ GAME END ~~~")

    return True


def main() -> None:
    p1 = Player("Nic", "1337")
    p2 = Player("Yella", "69")
    p3 = Player("rando", "this is a number")
    p4 = Player("yup", "3333333333")

    players = [p1, p2, p3, p4]

    test(players)


if __name__ == "__main__":
    main()
