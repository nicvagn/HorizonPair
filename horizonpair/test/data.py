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

from typing import List

from horizonpair.cfc import CfcId
from horizonpair.chess import Colour, Match, Player, Result
from horizonpair.gui.widget import (
    MatchWidget,
    PlayerWidget,
    RosterWidget,
    TournamentWidget,
)
from horizonpair.tournament import Roster, Round, Tournament


class TestData:
    """defines players, rosters and tournaments, Lists of objects to be used in tests"""

    players: List[Player] = [
        Player("Player 1", CfcId("111111")),
        Player("Player 2", CfcId("222222")),
        Player("Player 3", CfcId("333333")),
        Player("Player 4", CfcId("444444")),
        Player("Player 5", CfcId("555555")),
        Player("Player 6", CfcId("666666")),
        Player("Player 7", CfcId("777777")),
        Player("Player 8", CfcId("888888")),
        Player("Player 9", CfcId("999999")),
        Player("Player 10", CfcId("100000")),
        Player("Player 11", CfcId("110000")),
        Player("Player 12", CfcId("120000")),
        Player("Player 13", CfcId("130000")),
        Player("Player 14", CfcId("140000")),
        Player("Player 15", CfcId("150000")),
        Player("Player 16", CfcId("160000")),
        Player("Player 17", CfcId("170000")),
        Player("Player 18", CfcId("180000")),
        Player("Player 19", CfcId("190000")),
    ]

    rosters = [Roster(players[:6]), Roster(players[6:12]), Roster(players[12:18])]

    tournaments = [
        Tournament("Tournament 1", rosters[0]),
        Tournament("Tournament 1", rosters[1]),
        Tournament("Tournament 1", rosters[2]),
    ]
