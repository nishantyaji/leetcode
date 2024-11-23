# Problem 1861
import copy
from typing import List


class RotatingTheBox:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        # A lot of scope of improvement
        # I will prune and prim this code next time I work on this
        rows, cols = len(box), len(box[0])
        another = copy.deepcopy(box)
        for r in range(rows):
            for c in range(cols):
                another[r][c] = "."

        cnt = 0
        for r, row in enumerate(box):
            for c, cell in enumerate(row):
                if cell == "#":
                    cnt += 1

                if cell == "*":
                    another[r][c] = "*"
                    for i in range(cnt):
                        another[r][c - 1 - i] = "#"
                    cnt = 0

                if c == cols - 1:
                    for i in range(cnt):
                        another[r][c - i] = "#"
                    cnt = 0
        transpose = [["." for _ in range(rows)] for _ in range(cols)]
        for r, row in enumerate(another):
            for c, cell in enumerate(row):
                transpose[c][rows - 1 - r] = another[r][c]
        return transpose

if __name__ == '__main__':
    r = RotatingTheBox()
    print(r.rotateTheBox([["#", ".", "#"]]))
    print(r.rotateTheBox([["#", ".", "*", "."], ["#", "#", "*", "."]]))
    print(r.rotateTheBox(
        [["#", "#", "*", ".", "*", "."], ["#", "#", "#", "*", ".", "."], ["#", "#", "#", ".", "#", "."]]))
