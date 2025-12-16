# Problem 1523

class CountOddNumsInAnIntervalRange:
    def countOdds(self, low: int, high: int) -> int:
        low = low if low % 2 == 0 else low - 1
        high = high if high % 2 == 0 else high + 1
        return (high - low) // 2
