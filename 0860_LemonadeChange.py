from typing import List


class LemonadeChange:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = {5: 0, 10: 0, 20: 0}
        for b in bills:
            change[b] += 1
            if b == 20:
                if change[10] >= 1 and change[5] >= 1:
                    change[10] -= 1
                    change[5] -= 1
                elif change[5] >= 3:
                    change[5] -= 3
                else:
                    return False
            if b == 10:
                if change[5] >= 1:
                    change[5] -= 1
                else:
                    return False
        return True
