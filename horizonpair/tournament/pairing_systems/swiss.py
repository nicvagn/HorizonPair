#  swiss is a part of HorizonPair
#  HorizonPair is free software: you can redistribute it and/or modify it under the terms of the gnu general public license as published by the free software foundation, either version 3 of the license, or (at your option) any later version.
#
#  HorizonPair is distributed in the hope that it will be useful, but without any warranty; without even the implied warranty of merchantability or fitness for a particular purpose. see the gnu general public license for more details.
#
#  you should have received a copy of the gnu general public license along with HorizonPair. if not, see <https://www.gnu.org/licenses/>.

from horizonpair.chess import Match, Player
from horizonpair.tournament.pairing_systems.system import PairingSystem
from horizonpair.tournament.round import Round


class Swiss(PairingSystem):
    """The swiss system for pairing tournaments"""

    # TODO: this

    def pair(players: [Player]) -> Round:
        pass
