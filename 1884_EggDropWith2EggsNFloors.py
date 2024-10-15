# Problem 1884
import math


class EggDropWith2EggsNFloors:
    def twoEggDrop(self, n: int) -> int:
        return math.ceil((math.sqrt(8 * n + 1) - 1) / 2)
