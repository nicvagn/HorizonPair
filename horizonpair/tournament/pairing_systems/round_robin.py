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

from horizonpair.tournament import Roster, Round

# round robin
from horizonpair.tournament.pairing_systems.system import PairingSystem


class RoundRobin(PairingSystem):
    """The round robin pairing system for tournaments as defined by CFC"""

    def pair(self, round_number: int, roster: Roster) -> Round:
        """create the pairings"""
        number_of_players = roster.number_of_players
        assert number_of_players >= 2

        raise NotImplementedError
