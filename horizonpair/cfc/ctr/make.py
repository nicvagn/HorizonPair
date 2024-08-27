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
from horizonpair.chess import Match, Player

# make a ctr tournament report file
from horizonpair.exceptions import CtrCreationException
from horizonpair.tournament import Roster, Tournament
from horizonpair.tournament.pairing_systems import DoubleRoundRobin, RoundRobin, Swiss


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

        ctr: [str] = []
        ctr.append(
            f'"{t.name}","{t.province}","0","{pairing_abriviation}","{t.date}","{
                t.roster.number_of_players}","{t.td_cfc_id}",{t.to_cfc_id}"\n'
        )

        # add all matches to report
        for round in t.completed_rounds:
            for match in round.match_record:
                ctr.extend(make_match_report(match))

    def write_file(self) -> None:
        """write the ctr report to file"""
        try:
            assert self.ctr != []

        except AssertionError:
            print("make_ctr_report: asked to write ctr file but no ctr data")
            raise CtrCreationException("missing ctr data when asked to write file")

        # write the ctr report to file
        ctr_report = open("ctr_report.txt", "w")
        for line in ctr:
            ctr_report.write(line)
        ctr_report.close()

    def make_match_report(self, match: Match) -> [str]:
        """make a match part of ctr report file
        returns: a list of strings to be written to ctr_report one per line"""

        # make things cleaner
        m: Match = match

        res = "W" if m.winner == m.player1 else "L"
        return [
            f'"{m.player1.name}","{m.player1.cfc_id}","{m.player2.name}","{m.player2.cfc_id}","{res}"\n'
        ]


if __name__ == "__main__":

    player_list = [
        Player("player 1", "cfc id 1"),
        Player("player 2", "cfc id 2"),
        Player("player 3", "cfc id 3"),
        Player("player 4", "cfc id 4"),
    ]
    roster = Roster(player_list)
    t = Tournament(name="HorizonPair", province="SK", roster=roster)
    make_ctr_report(t)
