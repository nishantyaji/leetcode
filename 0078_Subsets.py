# Problem 78


from typing import List


class Subsets:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return [list(
            map(lambda y: y[1], list(filter(lambda x: x[0] == '1', zip(list(bin(i)[2:].rjust(len(nums), '0')), nums)))))
                for i in range(0, pow(2, len(nums)))]
