#  random is a part of HorizonPair
#  HorizonPair is free software: you can redistribute it and/or modify it under the terms of the gnu general public license as published by the free software foundation, either version 3 of the license, or (at your option) any later version.
#
#  HorizonPair is distributed in the hope that it will be useful, but without any warranty; without even the implied warranty of merchantability or fitness for a particular purpose. see the gnu general public license for more details.
#
#  you should have received a copy of the gnu general public license along with HorizonPair. if not, see <https://www.gnu.org/licenses/>.

from tournament.round import Round
from tournament.system import PairingSystem


class Random(PairingSystem):
    """The a 100% random pairing system for tournaments"""

    def pair(players: [Player]) -> Round:
        """create the pairings randomly"""
        number_of_players = len(players)
        assert number_of_players >= 2

        if number_of_players % == 1:
            # TODO: GIVE BYE

        # randomize the order of the list
        random.shuffle(players)

        # go from 0 to number_of_players by steps of 2 
        for n in range(0, number_of_players, 2):

            if number_of_players - n < 2:
                # if we cannot take 2 players from the unpaired players, give a bye

                # give a bye

                break

            # make pairing of n and n + 1 players




