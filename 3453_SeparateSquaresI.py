# Problem 3453
from typing import List


class SeparateSquaresI:
    def separateSquares(self, squares: List[List[int]]) -> float:
        s, e = 0, 1000000000
        st  = set()
        while s < e:
            m = (s + e) / 2
            print(m)
            if (s, e) in st:
                break
            st.add((s, e))
            [b, a] = self.total(squares, m)
            if b - a >= 0:
                e = m
            else:
                s = m
        return s

    def areas(self, square: List[int], line: int) -> list[float]:
        area = square[2] * square[2]
        below, above = 0, 0

        if line >= square[1] + square[2]:
            return [area, 0]
        elif line <= square[1]:
            return [0, area]
        return [(line - square[1]) * area / square[2], (square[1] +square[2]- line) * area / square[2]]

    def total(self, squares: List[List[int]], line: int) -> list[float]:
        below, above = 0, 0
        for s in squares:
            b, a = self.areas(s, line)
            below += b
            above += a
        return [below, above]


if __name__ == '__main__':
    s = SeparateSquaresI()
    print(s.total([[0,0,1],[2,2,1]], 1))
    print(s.separateSquares([[0,0,1],[2,2,1]]))
    print(s.separateSquares([[0,0,2],[1,1,1]]))
