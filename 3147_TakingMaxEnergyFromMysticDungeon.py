# Problem 3147
import sys
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

    def maximumEnergy2(self, energy: List[int], k: int) -> int:
        mx = -sys.maxsize
        dp = [-sys.maxsize] * k
        n = len(energy)
        for i in range(n - 1, -1, -1):
            mod = i % k

            if dp[mod] == -sys.maxsize:
                dp[mod] = energy[i]
            else:
                dp[mod] += energy[i]
            mx = max(mx, dp[mod])
        return mx

if __name__ == '__main__':
    w = TakingMaxEnergyFromMysticDungeon()
    print(w.maximumEnergy([5, 2, -10, -5, 1], 3))
    print(w.maximumEnergy([-2, -3, -1], 2))
