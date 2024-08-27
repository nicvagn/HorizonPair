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

from horizonpair.chess.match import Match
from horizonpair.chess.player import Player
from horizonpair.tournament.round import Round


class PairingSystem:
    """A pairing system to pair a chess tournament. This is a base class to be expanded on."""

    def pair(round_number: int, players: [Player]) -> Round:
        """pair a list of players into a round"""
        raise NotImplementedError()

    def make_match(white: Player, black: Player) -> Match:
        """make a chess match between two players"""
        return Match(white_player=white, black_player=black)
