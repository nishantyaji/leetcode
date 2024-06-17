# Problem 376
from typing import List


class WiggleSequence:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        # always add the first element
        result = [nums[0]]
        prev = nums[0]

        for num in nums[1:]:
            if num == prev:
                continue
            else:
                if num > prev and prev < result[-1]:
                    result.append(prev)
                elif num < prev and prev > result[-1]:
                    result.append(prev)
            prev = num

        if nums[-1] != result[-1]:
            result.append(nums[-1])

        return len(result)


if __name__ == '__main__':
    w = WiggleSequence()
    print(w.wiggleMaxLength(

        [33, 53, 12, 64, 50, 41, 45, 21, 97, 35, 47, 92,
         39, 0, 93, 55, 40, 46, 69, 42, 6, 95, 51, 68, 72,
         9, 32, 84, 34, 64, 6, 2, 26, 98, 3, 43, 30, 60, 3,
         68, 82, 9, 97, 19, 27, 98, 99, 4, 30, 96, 37, 9,
         78, 43, 64, 4, 65, 30, 84, 90, 87, 64, 18, 50,
         60, 1, 40, 32, 48, 50, 76, 100, 57, 29, 63, 53,
         46, 57, 93, 98, 42, 80, 82, 9, 41, 55, 69, 84,
         82, 79, 30, 79, 18, 97, 67, 23, 52, 38, 74, 15]

    ))
    print(w.wiggleMaxLength([3, 3, 3, 2, 5]))
    print(w.wiggleMaxLength([0, 0, 0]))

    print(w.wiggleMaxLength([1, 7, 4, 9, 2, 5]))
    print(w.wiggleMaxLength([1, 17, 5, 10, 13, 15, 10, 5, 16, 8]))
    print(w.wiggleMaxLength([1, 2, 3, 4, 5, 6, 7, 8, 9]))
