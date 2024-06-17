# Problem 2225
from collections import Counter
from typing import List


class FindPlayersWithZeroOrOneLosses:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners = []
        losers = []
        for match in matches:
            winners.append(match[0])
            losers.append(match[1])
        winners_counter = Counter(winners)
        losers_counter = Counter(losers)

        one_loser = [k for k, v in losers_counter.items() if v == 1]
        no_loser = [k for k, v in winners_counter.items() if k not in losers_counter]
        one_loser.sort()
        no_loser.sort()
        return [no_loser, one_loser]
