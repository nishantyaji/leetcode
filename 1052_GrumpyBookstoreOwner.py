from typing import List


class GrumpyBookstoreOwner:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:

        try:
            l_index, r_index = grumpy.index(1), len(grumpy) - 1 - grumpy[::-1].index(1)
        except ValueError:
            return sum(customers)

        u_limit, l_limit = min(r_index, len(customers) - minutes), max(0, l_index - minutes + 1)
        grumpy_cust = [abs(grumpy[i] - 1) * n for i, n in enumerate(customers)]
        left_sum, present, right_sum = sum(grumpy_cust[:l_limit]), sum(customers[l_limit:l_limit + minutes]), sum(grumpy_cust[l_limit + minutes:])
        result = run_sum = left_sum + present + right_sum
        for i in range(l_limit+1, u_limit + 1):
            if i >= 1:
                run_sum = run_sum + grumpy_cust[i-1] - customers[i-1] + customers[i + minutes - 1] - grumpy_cust[i + minutes - 1]
                result = max(result, run_sum)
        return result


if __name__ == '__main__':
    g = GrumpyBookstoreOwner()
    print(g.maxSatisfied([1, 0, 1, 2, 1, 1, 7, 5], [0, 1, 0, 1, 0, 1, 0, 1], 3))
    # 16
    print(g.maxSatisfied([2, 6, 6, 9], [0, 0, 1, 1], 1))
    # 17
    print(g.maxSatisfied([1], [0], 1))
    # 1
    print(g.maxSatisfied([10, 1, 7], [0, 0, 0], 2))
    # 18
