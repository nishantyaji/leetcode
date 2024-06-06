# Problem 846
from typing import List


class HandOfStraights:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        this_min, this_max = 1000000001, 0
        for h in hand:
            this_min = min(this_min, h)
            this_max = max(this_max, h)

        while hand:
            just_one = len(hand) == groupSize
            min_set, max_set, new_hand, new_min, new_max = set(), set(), [], 1000000001, 0
            for h in hand:
                if h <= this_min + groupSize - 1 and h not in min_set:
                    min_set.add(h)
                elif h >= this_max - groupSize + 1 and h not in max_set:
                    max_set.add(h)
                else:
                    new_hand.append(h)
                    new_min = min(new_min, h)
                    if not just_one:
                        new_max = max(new_max, h)
            if len(min_set) != groupSize or (not just_one and len(max_set) != groupSize):
                return False
            hand, this_min, this_max = new_hand, new_min, new_max
        return True
