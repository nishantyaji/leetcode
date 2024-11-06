# Problem 3011
from typing import List


class FindIfArrayCanBeSorted:
    def canSortArray(self, nums: List[int]) -> bool:

        # Check the solution in the editorial
        # Especially the solution that emulates the bubble sort (with extra condition)
        # and checks at the end whether the input list is sorted

        # Wrote this while suffering severe migraine. I need to look at it later.

        def num_one_bits(numm):
            return sum([int(i) for i in format(numm, "b")])

        nums_sorted = sorted(nums)
        sorted_dict = {x: i for i, x in enumerate(nums_sorted)}
        out_sort, rev_dict, vals = [], {}, []
        for i in range(len(nums)):
            vals.append(num_one_bits(nums[i]))
            if nums_sorted[i] != nums[i]:
                out_sort.append(i)

        for idx in out_sort:
            mn, mx = min(idx, sorted_dict[nums[idx]]), max(idx, sorted_dict[nums[idx]])
            st = set()
            for j in range(mn, mx + 1):
                st.add(vals[j])
            if len(st) > 1:
                return False

        if len(out_sort)  == 1:
            return False

        return True




if __name__ == '__main__':
    f = FindIfArrayCanBeSorted()
    print(f.canSortArray([112,146,81]))
    print(f.canSortArray([256,255,255]))
    print(f.canSortArray([75, 34, 30]))
    print(f.canSortArray([8, 4, 2, 30, 15]))
