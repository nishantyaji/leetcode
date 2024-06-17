import functools
from bisect import bisect_right
from typing import List


class MaxTotalRewardUsingOperationsI:
    def maxTotalReward2(self, rewardValues: List[int]) -> int:
        # This is not my solution
        # I have copied this solution here : because I find it elegant
        # Elegance in algo and usage of python
        v = sorted(set(rewardValues))

        @functools.cache
        def f(x):
            i = bisect_right(v, x)
            if i == len(v):
                return x
            return max(f(x + v[j]) for j in range(i, len(v)))

        return f(0)

    def maxTotalReward(self, rewardValues: List[int]) -> int:
        # Unfortunately I could not solve it during the contest.
        # Curse my brain fog and innate inability!
        # Following up on the clues and hints littered on this site -
        rewardValues = list(set(rewardValues))
        rewardValues.sort()

        @functools.cache
        def recurse(index: int, cum_sum: int) -> int:
            # End condition
            # 1 : when the last element of the sorted rewards has been considered and we increment index
            #       In this case we take the cumulative sum till now
            # 2: when the the cumulative sum is larger than the largest reward
            #       In this case we cannot choose reward because of the rewardValues[i] > cum_sum condition
            if index >= len(rewardValues) or cum_sum > rewardValues[-1]:
                return cum_sum

            # choose present index
            chosen, not_chosen = 0, 0
            if index == len(rewardValues) - 1:
                pass
            if rewardValues[index] > cum_sum:
                chosen = recurse(index + 1, cum_sum + rewardValues[index])
            not_chosen = recurse(index + 1, cum_sum)

            return max(chosen, not_chosen)

        return recurse(0, 0)


if __name__ == '__main__':
    w = MaxTotalRewardUsingOperationsI()
    print(w.maxTotalReward([1, 6, 4, 3, 2]))
    # 11
    print(w.maxTotalReward([7, 8, 3, 20]))
    # 35
    print(w.maxTotalReward([1, 1, 3, 3]))
    # 4
