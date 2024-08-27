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

# make a ctr tournament report file
from horizonpair.app.exceptions import CtrCreationException
from horizonpair.chess import Match, Player, Result
from horizonpair.tournament import Roster, Tournament
from horizonpair.tournament.pairing_systems import (
    DoubleRoundRobin,
    Random,
    RoundRobin,
    Swiss,
)


class CTR:
    """CTR is a wrapper class for CTR (Tournament Report) File format"""

    def __init__(self, tournament: Tournament) -> None:
        # make things cleaner
        t: Tournament = tournament

        # make sure the tournament has requisite data
        try:
            assert t.roster is not None
            assert t.roster.number_of_players > 0
            assert t.completed_rounds is not None
            assert t.pairing_system is not None
            assert t.td_cfc_id is not None
            assert t.province is not None
            assert t.date is not None

        except AssertionError:
            print(f"make_ctr_report: missing tournament data in {t.name}")
            raise CtrCreationException("missing tournament data.")

        # get the pairing abbreviation
        if tournament.pairing_system is Swiss:
            pairing_abriviation = "S"
        else:
            # Round Robin is default, I think this works ie: I think there are only 2 options
            pairing_abriviation = "R"

        self.ctr: [str] = []
        self.ctr.append(
            f'"{t.name}","{t.province}","0","{pairing_abriviation}","{t.date}","{
                t.roster.number_of_players}","{t.td_cfc_id}","{t.to_cfc_id}"'
        )

        # add all matches to report
        for round in t.completed_rounds:
            for match in round.matches:
                match_report = self.make_match_report(match, match.white_player)
                match_report += self.make_match_report(match, match.black_player)
                # append both players match reports to main report
                for line in match_report:
                    self.ctr.append(line)

    def write_file(self) -> None:
        """write the ctr report to file.
        side effect: creates file 'ctr_report.crt' in current directory.
                     If file already exists, it will be overwritten.
        """

        # make sure ctr data has been created
        try:
            assert self.ctr != []

        except AssertionError:
            print("make_ctr_report: asked to write ctr file but no ctr data")
            raise CtrCreationException("missing ctr data when asked to write file")

        # write the ctr report to file
        ctr_report = open("ctr_report.crt", "w")
        for line in ctr:
            ctr_report.write(line)
        ctr_report.close()

    def make_match_report(self, match: Match, player: Player) -> [str]:
        """make a match part of ctr report file for a given player
        returns: a list of strings to be written to ctr_report one per line"""

        match_winner = match.get_winner()

        if match_winner == player:
            res = "W"
            poins = 1
        elif match_winner is None:
            res = "D"
            poins = 0.5
        else:
            res = "L"
            poins = 0

        # match report
        match_report: [str] = []

        # line 1
        match_report.append(f'"{player.cfc_id}"')

        # line 2
        match_report.append(f'"{res}","0"')

        # line 3
        match_report.append(f'"{poins}"')

        return match_report


# TESTING
if __name__ == "__main__":

    player_list = [
        Player("player 1", "111111"),
        Player("player 2", "222222"),
        Player("player 3", "333333"),
        Player("player 4", "444444"),
    ]
    roster = Roster(player_list)
    t = Tournament(
        name="HorizonPair", province="SK", roster=roster, pairing_system=Random()
    )
    print("=== matches ===")
    for i in range(5):
        print(f"Round {i+1}:")
        t.current_round = t.pairing_system.pair(i, roster)

        # conclude all the matches
        for match in t.current_round.matches:
            match.conclude(Result.DRAW)
            print(match)

        t.completed_rounds.append(t.current_round)

    print("=== ctr report ===")
    ctr = CTR(t)
    for line in ctr.ctr:
        print(line)
