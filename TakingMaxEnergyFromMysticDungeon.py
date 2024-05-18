# Problem 3147

from typing import List


class TakingMaxEnergyFromMysticDungeon:

    def maximumEnergy(self, energy: List[int], k: int) -> int:
        dp = [0] * len(energy)
        max_all = -1001
        for i in range(len(energy) - 1, len(energy) - k - 1, -1):
            dp[i] = energy[i]
            max_all = max(dp[i], max_all)

        for i in range(len(energy) - k - 1, -1, -1):
            dp[i] = energy[i] + dp[i + k]
            max_all = max(dp[i], max_all)

        return max_all


if __name__ == '__main__':
    w = TakingMaxEnergyFromMysticDungeon()
    print(w.maximumEnergy([5, 2, -10, -5, 1], 3))
    print(w.maximumEnergy([-2, -3, -1], 2))
