# Problem 3178

class FindChildWhoHasBallAfterKSeconds:

    def numberOfChild(self, n: int, k: int) -> int:
        q, r = k // (n-1), k % (n-1)
        return r if q % 2 == 0 else (n - 1 - r)


if __name__ == '__main__':
    w = FindChildWhoHasBallAfterKSeconds()
    print(w.numberOfChild(2, 1))
    print(w.numberOfChild(3, 5))
    print(w.numberOfChild(5, 6))
    print(w.numberOfChild(4, 2))
    print(w.numberOfChild(5, 12))
    print(w.numberOfChild(5, 8))
