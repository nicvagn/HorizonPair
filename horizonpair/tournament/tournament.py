#  tournament is a part of HorizonPair
#  HorizonPair is free software: you can redistribute it and/or modify it under the terms of the gnu general public license as published by the free software foundation, either version 3 of the license, or (at your option) any later version.
#
#  HorizonPair is distributed in the hope that it will be useful, but without any warranty; without even the implied warranty of merchantability or fitness for a particular purpose. see the gnu general public license for more details.
#
#  you should have received a copy of the gnu general public license along with HorizonPair. if not, see <https://www.gnu.org/licenses/>.

from tournament.pairing_systems.system import PairingSystem
from tournament.round import Round


class Tournament:
    """A chess tournament, consisting of rounds, games, and matches"""

    def __init__(self, number_of_rounds: int, pairing_system: PairingSystem) -> None:
        self.number_of_rounds = number_of_rounds
        self.completed_rounds: [Round] = None
        self.pairing_system = pairing_system
        self.match_record = List[Matches]

    def __str__(self) -> str:
        """give a str representation of the tournament"""
        rep = (
            f"tournament with { self.pairing_system } as the pairing system.\n"
            + f"and { self.number_of_rounds } rounds.\n"
            + f"completed rounds: { self.completed_rounds }\n"
            + f"match record: { self.match_record }\n"
        )
        return rep
