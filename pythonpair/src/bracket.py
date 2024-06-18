"""
    This file is a part of Horizon Pair

    Horizon Pair is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

    This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

    You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>. 
"""

from typing import List

from match import Match


class Bracket:
    """a bracket in a chess tournament"""

    def __init__(matches: List[Match]) -> None:
        self.matches: List[Match]
        # are all players in bracket at the same score
        self.homogeneous: bool = None  # TODO:
