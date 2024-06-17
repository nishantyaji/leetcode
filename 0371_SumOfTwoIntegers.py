# Problem 371
import math


class SumOfTwoIntegers:
    def getSum(self, a: int, b: int) -> int:
        return int(math.log2((2**a)*(2**b)))


if __name__ == '__main__':
    s = SumOfTwoIntegers()
    print(s.getSum(1, 2))
    print(s.getSum(2, 3))
