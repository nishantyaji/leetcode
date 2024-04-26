# Problem 509

class FibonacciNumbers:
    def fib(self, n: int) -> int:
        f = [0, 1]
        if n < 1:
            return f[n]
        for r in range(1, n):
            f.append(f[0] + f[1])
            f.pop(0)
        return f[1]
