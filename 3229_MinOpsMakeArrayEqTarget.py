# Problem 3229
from typing import List


class MinOpsMakeArrayEqTarget:

    def minimumOperations(self, nums: List[int], target: List[int]) -> int:
        ops = 0
        diffs = [nums[i] - target[i] for i in range(len(nums))]
        pos_diff = [x if x > 0 else 0 for x in diffs]
        neg_diff = [abs(x) if x < 0 else 0 for x in diffs]

        for diff in [pos_diff, neg_diff]:
            ops += diff[0]
            for i in range(1, len(diff)):
                if diff[i] > diff[i - 1]:
                    ops += diff[i] - diff[i-1]

        return ops

    def minimumOperations2(self, nums: List[int], target: List[int]) -> int:
        # This is suboptimal and gives Time Limit Exceeded
        # This was my first approach though
        ops = 0
        diff = [nums[i] - target[i] for i in range(len(nums))]

        while True:
            length, max_len, low, up, op, max_low, max_up, max_op = -1, -1, -1, -1, 0, -1, -1, 0
            inc, dec, changed = False, False, False

            for i in range(len(nums)):
                if diff[i] > 0:
                    changed = True
                    if inc:
                        length += 1
                        if length > max_len:
                            max_len, up = length, i + 1
                            max_low, max_up, max_op = low, up, 1
                    else:
                        length, low, up, inc, dec = 1, i, i + 1, True, False
                        if length > max_len:
                            max_low, max_up, max_op = low, up, 1

                if diff[i] < 0:
                    changed = True
                    if dec:
                        length += 1
                        if length > max_len:
                            max_len, up = length, i + 1
                            max_low, max_up, max_op = low, up, -1
                    else:
                        length, low, up, inc, dec = 1, i, i + 1, False, True
                        if length > max_len:
                            max_low, max_up, max_op = low, up, -1

            if not changed:
                break

            ops += 1
            for j in range(max_low, max_up):
                diff[j] -= max_op

        return ops


if __name__ == '__main__':
    m = MinOpsMakeArrayEqTarget()
    print(m.minimumOperations([9, 2, 6, 10, 4, 8, 3, 4, 2, 3], [9, 5, 5, 1, 7, 9, 8, 7, 6, 5]))
    # 20
    print(m.minimumOperations([1, 1, 3, 3, 2, 3, 3, 1, 2], [2, 3, 2, 1, 3, 2, 3, 1, 1]))
    # 7
    print(m.minimumOperations([3, 5, 1, 2], [4, 6, 2, 4]))
    # 2
    print(m.minimumOperations([1, 3, 2], [2, 1, 4]))
    # 5
