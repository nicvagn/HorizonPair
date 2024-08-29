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

import random

from horizonpair.chess import Match, Player
from horizonpair.tournament.pairing_systems.system import PairingSystem
from horizonpair.tournament.roster import Roster
from horizonpair.tournament.round import Round


class Random(PairingSystem):
    """The a 100% random pairing system for tournaments"""

    def pair(self, round_number: int, roster: Roster) -> Round:
        """create the pairings randomly"""
        number_of_players = roster.number_of_players
        assert number_of_players >= 2

        if (number_of_players % 2) == 1:
            # TODO: GIVE BYE
            # if there is an odd number of players, give a bye
            raise NotImplementedError

        players = roster.player_list

        # randomize the order of the list
        random.shuffle(players)

        # a place for the matches
        matches: list[Match] = []
        # go from 0 to number_of_players by steps of 2
        for n in range(0, number_of_players, 2):

            if number_of_players - n < 2:
                # if we cannot take 2 players from the unpaired players, give a bye
                raise NotImplementedError

            # make pairing of n and n + 1 players
            matches.append(Match(players[n], players[n + 1], round=round_number))

        return Round(round_number, matches)
