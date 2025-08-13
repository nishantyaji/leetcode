# Problem 326

import functools


class PowerOfThree:
    @functools.cache
    def get_set(self):
        x, st = 1, {1}
        while x <= pow(2, 31):
            x *= 3
            st.add(x)
        return st

    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        st = self.get_set()
        return n in st
