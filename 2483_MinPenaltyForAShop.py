# Problem 2483

class MinPenaltyForAShop:
    def bestClosingTime(self, customers: str) -> int:
        y = sum([1 if x == "Y" else 0 for x in customers])
        penalty = y
        ans, index = penalty, 0
        for i in range(1, len(customers) + 1):
            penalty = penalty + 1 if customers[i - 1] == "N" else penalty - 1
            if penalty < ans:
                ans = penalty
                index = i
        return index
