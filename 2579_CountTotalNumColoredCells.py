# Problem 2579

class CountTotalNumColoredCells:
    def coloredCells(self, n: int) -> int:
        return 1 + (2 * n * (n - 1))
