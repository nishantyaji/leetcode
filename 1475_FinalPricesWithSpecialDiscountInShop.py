# Problem 1475
from typing import List


class FinalPricesWithSpecialDiscountInShop:

    def finalPrices(self, prices: List[int]) -> List[int]:
        # O(n) using stack
        n = len(prices)
        res = [0] * n
        stack = []
        for i in range(n - 1, -1, -1):
            res[i] = prices[i]
            if stack:
                while stack and stack[-1] > prices[i]:
                    stack.pop()
                if stack:
                    res[i] = prices[i] - stack[-1]
            stack.append(prices[i])
        return res

    def finalPricesSlow(self, prices: List[int]) -> List[int]:
        # O(n^2) time complexity
        n = len(prices)
        res = [0] * n
        for i in range(n):
            res[i] = prices[i]
            for j in range(i + 1, n):
                if prices[j] <= prices[i]:
                    res[i] = prices[i] - prices[j]
                    break
        return res


if __name__ == '__main__':
    f = FinalPricesWithSpecialDiscountInShop()
    print(f.finalPrices([8, 4, 6, 2, 3]))
