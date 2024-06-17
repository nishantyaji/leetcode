# Problem 51
import copy
from typing import List


class NQueens:

    def __init__(self):
        self.n = 0
        self.result = []

    def solveNQueens(self, n: int) -> List[List[str]]:
        self.n = n
        flags = [[False for y in range(n)] for x in range(n)]
        answer = []
        self.recurse(flags, 0, answer)
        return self.result

    def recurse(self, flags: List[List[bool]], row: int, answer: List[List[int]]):
        for c in range(self.n):
            if not flags[row][c]:
                answer_copy = list(answer)
                flags_copy = copy.deepcopy(flags)
                answer_copy.append([row, c])
                if row == self.n - 1:
                    self.append_answer(answer_copy)
                else:
                    self.update_flags(flags_copy, row, c)
                    self.recurse(flags_copy, row + 1, answer_copy)

    def append_answer(self, answer: List[List[int]]):
        board = [["." for y in range(self.n)] for x in range(self.n)]
        board_str = []
        for [r, c] in answer:
            board[r][c] = "Q"
            board_str.append("".join(board[r]))
        self.result.append(board_str)

    def update_flags(self, flags: List[List[bool]], row: int, col: int):
        for i in range(self.n):
            flags[row][i] = True
            flags[i][col] = True

        r, c = row - 1, col - 1
        while self.n - 1 >= r >= 0 and self.n - 1 >= c >= 0:
            flags[r][c] = True
            r -= 1
            c -= 1

        r, c = row + 1, col + 1
        while self.n - 1 >= r >= 0 and self.n - 1 >= c >= 0:
            flags[r][c] = True
            r += 1
            c += 1

        r, c = row + 1, col - 1
        while self.n - 1 >= r >= 0 and self.n - 1 >= c >= 0:
            flags[r][c] = True
            r += 1
            c -= 1

        r, c = row - 1, col + 1
        while self.n - 1 >= r >= 0 and self.n - 1 >= c >= 0:
            flags[r][c] = True
            r -= 1
            c += 1


if __name__ == '__main__':
    n = NQueens()
    print(n.solveNQueens(9))
