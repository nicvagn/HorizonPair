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

from horizonpair.cfc.id import CfcId
from horizonpair.chess import Match, Player
from horizonpair.tournament.pairing_systems.random import Random
from horizonpair.tournament.pairing_systems.system import PairingSystem
from horizonpair.tournament.roster import Roster
from horizonpair.tournament.round import Round


class Tournament:
    """A chess tournament, consisting of rounds, games, and matches"""

    def __init__(
        self,
        name: str = "HorizonPair",
        roster: Roster = None,
        acceleration_method=None,
        number_of_rounds: int = None,
        pairing_system: PairingSystem = None,
        province: str = "SK",
        td_cfc_id: CfcId = "000000",
        to_cfc_id: CfcId = "000000",
        date="0000/00/00",
    ) -> None:
        # ensure all parameters are acounted for (some are left with default values for now)
        assert roster is not None
        assert pairing_system is not None

        # init attributes
        self.name: str = name
        self.roster: Roster = roster
        self.acceleration_method = acceleration_method
        self.number_of_rounds: int = number_of_rounds
        self.pairing_system: PairingSystem = pairing_system
        self.province: str = province
        self.td_cfc_id: CfcId = td_cfc_id
        self.to_cfc_id: CfcId = to_cfc_id
        self.date = date

        # other tournament attributes:

        # start at the first round
        self.current_round_num: int = 1
        # passed rounds
        self.completed_rounds: [Round] = list()
        # pair the first round of the tournament
        self.current_round: Round = self.pairing_system.pair(
            self.current_round_num, self.roster
        )

    def __str__(self) -> str:
        """give a str representation of the tournament"""
        rep = (
            f"tournament with { self.pairing_system } as the pairing system.\n"
            + f"rounds: { self.number_of_rounds }\n"
            + f"roster: { self.roster }\n"
            + f"completed rounds: { self.completed_rounds }\n"
        )
        return rep

    def pair_next_round(self) -> Round:
        """pair the next round in the tournament
        side effects: +1 to the current round, add current round to completed rounds
        """
        self.completed_rounds.append(self.current_round)
        self.current_round_num += 1

        # pair the next round according to the pairing system
        new_round: Round = self.pairing_system.pair(self.current_round_num, self.roster)

        # add the newly completed round to the completed rounds
        self.completed_rounds.append(self.current_round)

        # update the current round to the newly paired one
        self.current_round = new_round

        return self.current_round

    def get_roster(self) -> Roster:
        """return the roster of the tournament"""
        return self.roster

    def get_name(self) -> str:
        """return the name of the tournament"""
        return self.name


def test() -> bool:
    t = Tournament(4, Random())
    return True


if __name__ == "__main__":
    test()
