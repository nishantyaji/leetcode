# Problem 3153. Sum of Digit Differences of All Pairs

from typing import List


class SumDigitDiffOfAllPairs:
    def sumDigitDifferences(self, nums: List[int]) -> int:
        # list_of_dict_of_sets
        lodos = [None] * 9

        for num in nums:
            num_str = str(num)

            for i in range(len(num_str) - 1, -1, -1):
                index_digit = len(num_str) - 1 - i
                if lodos[index_digit] is None:
                    lodos[index_digit] = dict()
                if num_str[i] not in lodos[index_digit]:
                    lodos[index_digit][num_str[i]] = 0
                lodos[index_digit][num_str[i]] += 1

        result = 0
        for lodo in lodos:
            if lodo is not None and len(lodo) > 0:
                this_sum = 0
                for k, v in lodo.items():
                    this_sum += v
                temp_sum = 0
                for k, v in lodo.items():
                    temp_sum += v * (this_sum - v)
                temp_sum = temp_sum // 2
                result += temp_sum

        return result


if __name__ == '__main__':
    w = SumDigitDiffOfAllPairs()
    print(w.sumDigitDifferences([13, 23, 12]))
