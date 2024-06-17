# Problem 121
from typing import List


class BestTimeToBuyAndSellStock:
    def maxProfit(self, prices: List[int]) -> int:
        min = 1e6
        max_profit = 0
        for num in prices:
            if num < min:
                min = num
            else:
                temp = num - min
                if temp > max_profit:
                    max_profit = temp
        return max_profit


if __name__ == '__main__':
    b = BestTimeToBuyAndSellStock()
    print(b.maxProfit([7, 1, 5, 3, 6, 4]))
    print(b.maxProfit([7, 6, 4, 3, 1]))
