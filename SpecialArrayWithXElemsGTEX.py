from typing import List


class SpecialArrayWithXElemsGTEX:

    def specialArray(self, nums: List[int]) -> int:
        for i in range(0, min(len(nums) + 1, 1001)):
            if i == len([x for x in nums if x >= i]):
                return i
        return -1


if __name__ == '__main__':
    s = SpecialArrayWithXElemsGTEX()
    print(s.specialArray([0, 4, 3, 0, 4]))
