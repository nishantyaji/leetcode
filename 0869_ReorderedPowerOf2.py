# Problem 869
import functools
import math


class ReorderedPowerOf2:
    def reorderedPowerOf2(self, n: int) -> bool:
        st = self.get_set()
        print(st)
        return self.sort_str(n) in st

    @functools.cache
    def get_set(self):
        max_pow = math.ceil(math.log2(1000000000 + 1))
        st = set()
        for i in range(max_pow):
            st.add(self.sort_str(pow(2, i)))
        return st

    def sort_str(self, n: int):
        ls = list(str(n))
        ls.sort()
        return "".join(ls)
