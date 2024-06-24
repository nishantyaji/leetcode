# Problem 995

from typing import List


class MinNumOfKConsecutiveBitFlips:

    def minKBitFlips(self, nums: List[int], k: int) -> int:
        # My second approach which passed the muster
        # We go on flipping ints from left to right
        if k == 1:
            return sum(1 for n in nums if n == 0)

        result, i, run_sum = 0, 0, 0
        dq = [0] * k
        for i in range(len(nums) - k + 1):
            run_sum -= dq.pop(0)
            if (nums[i] + run_sum) % 2 == 0:
                dq.append(1)
                result += 1
                run_sum += 1
            else:
                dq.append(0)

        i += 1
        while i < len(nums):
            run_sum -= dq.pop(0)
            if (nums[i] + run_sum) % 2 == 0:
                return -1
            i += 1

        return result

    ######################################################
    #
    # Sub optimal solution
    #
    ######################################################
    def minKBitFlips2(self, nums: List[int], k: int) -> int:
        # This was my first approach. Resulted in Time Limit Exceeded
        def contains(long: List[int], short: List[int]):
            return long[:len(short)] == short

        def first_0(arr: List[int]):
            try:
                i = arr.index(0)
                return i
            except ValueError:
                return -1

        def flip(arr: List[int], index: int, k: int):
            if index >= len(arr) + 1 - k:
                return arr
            for i in range(k):
                arr[index + i] = 1 - arr[index + i]
            return arr

        result = 0
        ones, zeros = [1] * k, [0] * k
        while len(nums) >= k:
            if contains(nums, ones):
                nums = nums[k:]
            elif contains(nums, zeros):
                nums = nums[k:]
                result += 1

            idx = first_0(nums)
            if idx == -1:
                return result

            flip(nums, idx, k)
            if nums[idx] == 0:
                return -1
            else:
                result += 1

        return result if all(map(lambda x: x == 1, nums)) else -1


if __name__ == '__main__':
    m = MinNumOfKConsecutiveBitFlips()
    print(m.minKBitFlips([0, 1, 0], 1))
    print(m.minKBitFlips([1, 1, 0], 2))
    print(m.minKBitFlips([0, 0, 0, 1, 0, 1, 1, 0], 3))
