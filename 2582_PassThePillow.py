# Problem 2582

class PassThePillow:
    def passThePillow(self, n: int, time: int) -> int:
        # Solution is similar to problem 3178
        q, r = divmod(time, n - 1)
        return r + 1 if q % 2 == 0 else (n - r)
