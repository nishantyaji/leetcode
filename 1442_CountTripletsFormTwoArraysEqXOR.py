# Problem 1442

from typing import List


class CountTripletsFormTwoArraysEqXOR:
    # There are better algorithms than this O(n**3) implmentation
    def countTriplets(self, arr: List[int]) -> int:
        xor_table = []
        for i in range(len(arr)):
            this_xor = [arr[i]]
            for j in range(i + 1, len(arr)):
                this_xor.append(this_xor[-1] ^ arr[j])
            xor_table.append(this_xor)

        result = 0
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                for k in range(j, len(arr)):
                    if xor_table[j][k - j] == xor_table[i][j - 1 - i]:
                        result += 1

        return result


if __name__ == '__main__':
    c = CountTripletsFormTwoArraysEqXOR()
    print(c.countTriplets([2, 3, 1, 6, 7]))
    print(c.countTriplets([1, 1, 1, 1, 1]))
