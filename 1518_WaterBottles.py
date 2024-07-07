# Problem 1518

class WaterBottles:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        result = numBottles
        while numBottles >= numExchange:
            numBottles, not_used = divmod(numBottles, numExchange)
            result += numBottles
            numBottles += not_used
        return result


if __name__ == '__main__':
    w = WaterBottles()
    print(w.numWaterBottles(9, 3))
    # 13
    print(w.numWaterBottles(15, 4))
    # 19
