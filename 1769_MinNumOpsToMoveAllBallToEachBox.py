# Problem 1769
from typing import List


class MinNumOpsToMoveAllBallToEachBox:
    def minOperations(self, boxes: str) -> List[int]:
        ones = list(reversed([i for i, x in enumerate(boxes) if x == "1"]))
        length, total, right = len(ones), sum(ones), len(ones)
        res = [total]
        if ones and ones[-1] == 0:
            ones.pop()
            right -= 1
        for i in range(1, len(boxes)):
            this_val, exclude = res[-1], False
            if ones and ones[-1] == i:
                ones.pop()
                this_val -= 1
                right -= 1
                exclude = True
            this_val = this_val - right + (length - right - (1 if exclude else 0))
            res.append(this_val)
        return res


if __name__ == '__main__':
    m = MinNumOpsToMoveAllBallToEachBox()
    print(m.minOperations("110"))  # [1,1,3]
    print(m.minOperations("001011"))  # [11,8,5,4,3,4]
