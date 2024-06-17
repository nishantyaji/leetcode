# Problem 66
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


if __name__ == '__main__':
    p = PlusOne()
    print(p.plusOne([9, 9]))
