#  tournament is a part of HorizonPair
#  HorizonPair is free software: you can redistribute it and/or modify it under the terms of the gnu general public license as published by the free software foundation, either version 3 of the license, or (at your option) any later version.
#
#  HorizonPair is distributed in the hope that it will be useful, but without any warranty; without even the implied warranty of merchantability or fitness for a particular purpose. see the gnu general public license for more details.
#
#  you should have received a copy of the gnu general public license along with HorizonPair. if not, see <https://www.gnu.org/licenses/>.

from horizonpair.chess import Match, Player
from horizonpair.tournament.pairing_systems.random import Random
from horizonpair.tournament.pairing_systems.system import PairingSystem
from horizonpair.tournament.roster import Roster
from horizonpair.tournament.round import Round


class Tournament:
    """A chess tournament, consisting of rounds, games, and matches"""

    def __init__(
        self,
        number_of_rounds: int,
        pairing_system: PairingSystem,
        roster: Roster,
        name: str,
    ) -> None:
        self.number_of_rounds = number_of_rounds
        self.completed_rounds: [Round] = None
        self.pairing_system = pairing_system
        self.match_record = list[Match]
        self.roster: Roster = roster
        self.name: str = name
        # start at the first round
        self.current_round = 1

    def __str__(self) -> str:
        """give a str representation of the tournament"""
        rep = (
            f"tournament with { self.pairing_system } as the pairing system.\n"
            + f"rounds: { self.number_of_rounds }\n"
            + f"roster: { self.roster }\n"
            + f"completed rounds: { self.completed_rounds }\n"
            + f"match record: { self.match_record }\n"
        )
        return rep

    def pair_round(self) -> Round:
        """pair a round in the tournament"""
        # pair a new Round according to the pairing system
        new_round: Round = self.pairing_system.pair(self.current_round, self.roster)

        return new_round

    def get_roster(self) -> Roster:
        """return the roster of the tournament"""
        return self.roster

    def get_name(self) -> str:
        """return the name of the tournament"""
        return self.name


def test() -> bool:
    t = Tournament(4, Random)
    return True


if __name__ == "__main__":
    test()
