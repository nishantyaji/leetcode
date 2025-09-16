# Problem 2197
from typing import List


class ReplaceNonCoPrimeNumsInArray:

    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:

        stack = []
        for i, n in enumerate(nums):
            if stack:
                g = self.gcd(n, stack[-1])
                if g > 1:
                    stack.append(n)
                    while len(stack) > 1:
                        g = self.gcd(stack[-2], stack[-1])
                        if g > 1:
                            a = stack.pop()
                            b = stack.pop()
                            stack.append(self.lcm(a, b))
                        else:
                            break
                else:
                    stack.append(n)
            else:
                stack.append(n)

        return stack

    def lcm(self, a: int, b: int) -> int:
        g = self.gcd(a, b)
        return a * b // g

    def gcd(self, a: int, b: int):
        large = a if a > b else b
        small = large ^ a ^ b

        q, r = divmod(large, small)
        if r == 0:
            return small
        return self.gcd(small, r)


if __name__ == '__main__':
    r = ReplaceNonCoPrimeNumsInArray()
    print(r.replaceNonCoprimes([287, 41, 49, 287, 899, 23, 23, 20677, 5, 825]))  # [2009, 20677, 825]

    print(r.replaceNonCoprimes([2, 3] * 2 + [6, 6]))  # [6

    print(r.replaceNonCoprimes([2, 2, 1, 1, 3, 3, 3]))  # [2,1,1,3]

    print(r.replaceNonCoprimes([6, 4, 3, 2, 7, 6, 2]))  # [12,7,6]
    print(r.replaceNonCoprimes([7, 252, 7, 15, 2]))
    print(r.replaceNonCoprimes([252, 7, 15]))
    print(r.replaceNonCoprimes([252, 7, 15, 1, 1, 1, 1, 1]))
    print(r.replaceNonCoprimes([252, 7, 15, 1, 1, 1, 1]))
    print(r.replaceNonCoprimes([1, 1, 252, 7, 15, 11, 11]))
