# Problem 330
from typing import List


class PatchingArray:

    def minPatches2(self, nums: List[int], n: int) -> int:
        # This is copied
        # Not my solution.
        # Recommend this solution
        count = 0
        missing = 1
        i = 0

        while missing <= n:
            if i < len(nums) and nums[i] <= missing:
                missing += nums[i]
                i += 1
            else:
                missing += missing
                count += 1

        return count

    def minPatches3(self, nums: List[int], n: int) -> int:
        # This is copied
        # Not my solution.
        # Recommend this solution also
        num_patches, i, next_num_idx = 0, 1, 0
        chosen = 0
        while next_num_idx < len(nums):
            if i < nums[next_num_idx]:
                # add the missing number
                chosen += i
                num_patches += 1
            else:
                # we can simply jump to missing + nums[next..]
                # because we have contiguous till previous missing
                chosen += nums[next_num_idx]
                next_num_idx += 1

            if chosen >= n:
                break
            # this is the next one which is missing
            i = chosen + 1

        # after the end of the num loops we need to check if we have reached n
        while chosen < n:
            chosen = 2 * chosen + 1
            num_patches += 1

        return num_patches

    def minPatches(self, nums: List[int], n: int) -> int:
        # This is a code that I submitted
        # Gives TLE
        a_limit = min(nums[-1], n)
        a = AllPos(a_limit)
        uniq = set()
        repeat = []
        for x in nums:
            if x in uniq:
                repeat.append(x)
            else:
                uniq.add(x)
            a.add(x)
        result = 0
        while not a.is_complete():
            next_num = a.get_next()
            a.add(next_num)
            result += 1
        max_pos = a.get_max_among_contiguous()

        while max_pos < n:
            max_pos = 2 * max_pos + 1
            result += 1
        return result


class AllPos:
    def __init__(self, limit):
        self.all = set()
        for i in range(1, limit + 1):
            self.all.add(i)
        self.container = set()
        self.limit = limit

    def add(self, num):
        if not self.container:
            self.container.add(num)
            return
        new_set = {num}
        for x in self.container:
            new_set.add(x + num)
        self.container.update(new_set)

    def is_complete(self):
        return len(self.all - self.container) == 0

    def get_next(self):
        return min(self.all - self.container)

    def get_max_among_contiguous(self):
        this_max = self.limit
        while this_max + 1 in self.container:
            this_max += 1
        return this_max


if __name__ == '__main__':
    p = PatchingArray()
    print(p.minPatches([1, 2, 32], 2147483647))
    print(p.minPatches(
        [2, 3, 3, 4, 6, 8, 8, 10, 10, 10, 12, 13, 13, 14, 15, 15, 16, 17, 19, 20, 20, 21, 21, 21, 23, 23, 24, 25, 26,
         27, 27, 28, 28, 29, 29, 30, 30, 31, 31, 32, 32, 32, 36, 36, 38, 41, 41, 41, 43, 44, 46, 46, 46, 48, 48, 49, 50,
         51, 51, 52, 52, 53, 54, 55, 56, 56, 58, 58, 58, 59, 60, 60, 60, 61, 63, 63, 66, 66, 70, 70, 73, 74, 74, 75, 78,
         80, 81, 83, 85, 87, 87, 89, 89, 89, 90, 90, 92, 92, 96, 98],
        60844))
    # 5
    print(p.minPatches([1, 2, 3], 2147483647))
    # 29
    print(p.minPatches([1, 2, 31, 33], 2147483647))
    # 28
    print(p.minPatches([1, 3], 6))
    # 1
    print(p.minPatches([1, 5, 10], 20))
    # 2
    print(p.minPatches([1, 2, 2], 5))
    # 0
