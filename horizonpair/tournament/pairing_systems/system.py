#  system is a part of HorizonPair
#  HorizonPair is free software: you can redistribute it and/or modify it under the terms of the gnu general public license as published by the free software foundation, either version 3 of the license, or (at your option) any later version.
#
#  HorizonPair is distributed in the hope that it will be useful, but without any warranty; without even the implied warranty of merchantability or fitness for a particular purpose. see the gnu general public license for more details.
#
#  you should have received a copy of the gnu general public license along with HorizonPair. if not, see <https://www.gnu.org/licenses/>.

from chess.match import Match
from chess.player import Player
from tournament.round import Round


class PairingSystem:
    """A pairing system to pair a chess tournament. This is a base class to be expanded on."""

    def pair(players: [Player]) -> Round:
        """pair a list of players into chess Matches"""
        raise NotImplementedError()

    def make_match(white: Player, black: Player) -> Match:
        """make a chess match between two players"""
        return Match(white_player=white, black_player=black)
