# Problem 3145
import math
from typing import List


class FindProductsOfElemsOfBigArray:
    def findProductsOfElements(self, queries: List[List[int]]) -> List[int]:
        result = []

        for query in queries:
            if query[0] == query[1] and query[0] == 0:
                query_pow = 0
            else:
                [start_pow_2_trail, start_pow2_lead, full_star_int] = self.binary_search(query[0] - 1)
                [end_pow_2_trail, end_pow2_lead, full_end_int] = self.binary_search(query[1])
                lhs = full_end_int if end_pow_2_trail == 0 else full_end_int - 1
                query_pow = end_pow2_lead + self.pow_2(self.fn_list(lhs)) - self.pow_2(
                    self.fn_list(full_star_int)) + start_pow_2_trail
            result.append(pow(2, query_pow, query[2]))

        return result

    def pow_2(self, given: List[int]) -> int:
        res = 0
        for i in range(1, len(given)):
            res += given[i] * i
        return res

    def binary_search(self, index: int):
        start, end, mid = 1, 100000000000000, 0
        exact_match, temp_sum = False, 0
        while start <= end:
            mid = (start + end) // 2
            temp_sum = sum(self.fn_list(mid))
            if temp_sum == index + 1:
                exact_match = True
                break
            elif temp_sum > index + 1:
                end = mid - 1
            else:
                start = mid + 1

        trail_pow_of_2 = lead_pow_of_2 = 0
        if exact_match:
            pass
        else:
            diff = index + 1 - temp_sum
            if diff > 0:
                mid += 1
                temp_sum = sum(self.fn_list(mid))
                diff = index + 1 - temp_sum
            num_digits = int(math.log2(mid)) + 1
            base, pow_window = 1, []
            for j in range(0, num_digits):
                if mid & base > 0:
                    pow_window.append(j)
                base = base << 1
            trail_pow_of_2 = sum(pow_window[diff:])
            lead_pow_of_2 = sum(pow_window[:diff])

        return [trail_pow_of_2, lead_pow_of_2, mid]

    def fn_list(self, num: int) -> List[int]:
        num_digits = int(math.log2(num)) + 1
        result = [0] * num_digits
        base, half_base = 2, 1
        for i in range(0, num_digits):
            q = num >> (i + 1)
            rem = num & base - 1
            r = rem - (half_base - 1) if rem >= half_base else 0
            result[i] = q * half_base + r
            half_base = base
            base = base << 1
        return result


if __name__ == '__main__':
    f = FindProductsOfElemsOfBigArray()
    print(f.findProductsOfElements([[0, 1, 1]]))
    # 0

    print(f.findProductsOfElements([[7, 11, 100]]))
    # 64

    print(f.findProductsOfElements([[7, 7, 4]]))
    # 2

    print(f.findProductsOfElements([[1, 3, 7]]))
    # 4

    print(f.findProductsOfElements([[2, 5, 3], [7, 7, 4]]))
    # [2,2]
