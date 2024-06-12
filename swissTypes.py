"""
    This file is a part of Horizon Pair

    Horizon Pair is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

    This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

    You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>. 
"""

"""implimentations of diffrent types of swiss system's. IE: FIDE (Dutch), limi Dubov, Burnstein, Olimpiad Pairing System"""

class SwissPairingSystem:
    """a base class for building swiss pairing systems"""

    def __init__(num_rounds: Int, players: List[Players]) -> None:
        """@param: num_players - number of rounds to be played in total in this tournament
        @param: players - list of all players in this tournament
        """
        self.num_rounds = num_rounds
        self.players = players
        self.num_players = players.length()
        self.round_num = 1  # always init on first round
    
    def submit_round(results: RoundResults) -> None:
        """submit the result's of a round.
        @side_effect: increments round number.
        """
        # save round results and increment round number
        self.round_results[self.round_num - 1] = results
        self.round_num += 1
        
        

class Dutch(SwissPairingSystem):
    """Dutch(FIDE) pairing system"""

