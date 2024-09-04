from horizonpair.cfc import CfcId, ctr
from horizonpair.chess import Colour, Match, Player, Result
from horizonpair.tournament import Roster, Round, Tournament
from horizonpair.tournament.pairing_systems import Swiss

players = [
    Player("one", CfcId("111111")),
    Player("two", CfcId("222222")),
    Player("three", CfcId("333333")),
    Player("four", CfcId("444444")),
]
roster = Roster(players=players)
# create a simple test Tournament
t = Tournament(
    name="test",
    roster=roster,
    pairing_system=Swiss(),
    number_of_rounds=1,
)

print(t)
match1 = Match(white_player=players[0], black_player=players[1])
match1.conclude(Result.WHITE_WON)
match2 = Match(white_player=players[2], black_player=players[3])
match2.conclude(Result.BLACK_WON)
round1 = Round(round_number=1, matches=[match1, match2])
t.completed_rounds.append(round1)

# geterate CTR from tournament we made
t_ctr = ctr.make.CTR(t)

print(t_ctr)
