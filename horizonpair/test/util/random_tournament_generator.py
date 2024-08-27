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

from horizonpair.cfc import CfcId
from horizonpair.chess import Match, Player
from horizonpair.tournament.pairing_systems import *
from horizonpair.tournament.roster import Roster
from horizonpair.tournament.round import Round
from horizonpair.tournament.tournament import Tournament

# generate a random tournament for testing purposes

# some players to work with
player1 = Player("player1 smith", CfcId("111111"))
player2 = Player("player2 smith", CfcId("222222"))
player3 = Player("player3 smith", CfcId("333333"))
player4 = Player("player4 smith", CfcId("444444"))
player5 = Player("player5 smith", CfcId("555555"))
player6 = Player("player6 smith", CfcId("666666"))
player7 = Player("player7 smith", CfcId("777777"))
player8 = Player("player8 smith", CfcId("888888"))
player9 = Player("player9 smith", CfcId("999999"))
player10 = Player("player10 smith", CfcId("100010"))
player11 = Player("player11 smith", CfcId("110011"))
player12 = Player("player12 smith", CfcId("120012"))
player13 = Player("player13 smith", CfcId("130013"))
player14 = Player("player14 smith", CfcId("140014"))
player15 = Player("player15 smith", CfcId("150015"))
player16 = Player("player16 smith", CfcId("160016"))

# create a roster
roster = Roster(
    [
        player1,
        player2,
        player3,
        player4,
        player5,
        player6,
        player7,
        player8,
        player9,
        player10,
        player11,
        player12,
        player13,
        player14,
        player15,
        player16,
    ]
)

# create a tournament
tournament = Tournament(
    name="HorizonPair Random Tournament",
    roster=roster,
    number_of_rounds=4,
    pairing_system=Random,
    province="SK",
)

tournament.pair_next_round()

print(tournament)
