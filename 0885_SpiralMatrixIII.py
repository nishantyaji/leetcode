# Problem 0885
from typing import List


class SpiralMatrixIII:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        st = set()
        for r in range(rows):
            for c in range(cols):
                st.add((r, c))

        st.remove((rStart, cStart))
        cntr = {"h": 1, "v": 1}
        order = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        dir = ["h", "v", "h", "v"]
        i, res = 0, [[rStart, cStart]]
        while st:
            o = order[i % 4]
            val = cntr[dir[i % 4]]
            valx, valy = o[0] * val, o[1] * val
            cntr[dir[i % 4]] = val + 1
            i = i + 1
            signx, signy = 1 if valx >= 0 else -1, 1 if valy >= 0 else -1
            for j in range(1, abs(valx) + 1):
                if (rStart + signx * j, cStart) in st:
                    st.remove((rStart + signx * j, cStart))
                    res.append([rStart + signx * j, cStart])
            for j in range(1, abs(valy) + 1):
                if (rStart, cStart + signy * j) in st:
                    st.remove((rStart, cStart + signy * j))
                    res.append([rStart, cStart + signy * j])
            rStart, cStart = rStart + valx, cStart + valy
        return res


if __name__ == '__main__':
    s = SpiralMatrixIII()
    print(s.spiralMatrixIII(5, 6, 1, 4))
    print(s.spiralMatrixIII(1, 4, 0, 0))
