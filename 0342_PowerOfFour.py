import functools


class PowerOfFour:
    @functools.cache
    def all_powers(self):
        st = set()
        for i in range(0, 16):
            st.add(pow(4, i))
        return st

    def isPowerOfFour(self, n: int) -> bool:
        return n in self.all_powers()
