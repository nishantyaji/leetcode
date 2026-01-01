# Problem 66
import functools
from typing import List


class PlusOne:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = []
        digits.reverse()
        carry = 0
        if digits[0] == 9:
            result.append(0)
            carry = 1
        else:
            result.append(digits[0] + 1)
        for num in digits[1:]:
            num = num + carry
            result.append(num % 10)
            if num > 9:
                carry = 1
            else:
                carry = 0
        if carry > 0:
            result.append(carry)
        result.reverse()
        return result

    def plusOne_oneline(self, digits: List[int]) -> List[int]:
        return list(map(int, list(str(functools.reduce(lambda x, y: 10 * x + y, digits) + 1))))


if __name__ == '__main__':
    p = PlusOne()
    print(p.plusOne([9, 9]))
