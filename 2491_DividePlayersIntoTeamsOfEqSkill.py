# Problem 2491
import collections
from typing import List


class DividePlayersIntoTeamsOfEqSkill:
    def dividePlayers(self, skill: List[int]) -> int:
        if len(skill) % 2 == 1:
            return -1
        len_pair, target = len(skill) // 2, sum(skill)
        if target % len_pair > 0:
            return -1

        target = target // len_pair
        cntr = collections.Counter(skill)

        exclude = set() if target % 2 == 1 else {target // 2}
        for x in skill:
            if (x in exclude and cntr[x] % 2 == 1) or (x not in exclude and cntr[x] != cntr[target - x]):
                return -1
        return sum([x * (target - x) for x in skill]) // 2


if __name__ == '__main__':
    d = DividePlayersIntoTeamsOfEqSkill()
    print(d.dividePlayers([3, 2, 5, 1, 3, 4]))
    print(d.dividePlayers([3, 4]))
    print(d.dividePlayers([1, 1, 2, 3]))
