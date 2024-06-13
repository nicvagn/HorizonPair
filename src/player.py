"""
    This file is a part of Horizon Pair

    Horizon Pair is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

    This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

    You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>. 
"""

from colour import Colour


class Player:
    """a player to be paired by Horizon Pair."""

    def __init__(name: str, id: int, rating: int, colour: Colour):
        """
        @param: name - name ..
        @param: id - CFC id of the player
        @param: rating - CFC rating of the player
        """
        self.name = name
        self.id = id
        self.rating = rating
        self.colour = colour
        self.completedMatches = None
        self.colourHistory: List[Colour] = None
        self.matchHistory: List[Match]
        self.score = 0

    def colour_preferance() -> Colour:
        """Get the colour preferance for this player"""
        # find the number of games of each colour
        black_games = 0
        white_games = 0
        for match in matchHistory:
            if match.black == self:
                black_games += 1
            else:
                white_games += 1
