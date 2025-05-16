# Problem 2094
import collections
import copy
from typing import List


class Finding3DigitEvenNumbers:

    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        cntr = collections.Counter(digits)
        keys = cntr.keys()

        keys_even = [k for k in keys if k % 2 == 0]
        res = set()
        for k in keys_even:
            cntr_copy = copy.deepcopy(cntr)
            cntr_copy[k] -= 1
            if cntr_copy[k] == 0:
                del cntr_copy[k]
            keys_non0 = [k for k in cntr_copy.keys() if k != 0]
            for kn0 in keys_non0:
                cntr_copy_copy = copy.deepcopy(cntr_copy)
                cntr_copy_copy[kn0] -= 1
                if cntr_copy_copy[kn0] == 0:
                    del cntr_copy_copy[kn0]

                mid = [kcc for kcc in cntr_copy_copy.keys()]
                for m in mid:
                    res.add("".join(list(map(str, [kn0, m, k]))))

        return list(map(int, list(sorted(res))))


if __name__ == '__main__':
    f = Finding3DigitEvenNumbers()
    print(f.findEvenNumbers([2,1,3,0]))