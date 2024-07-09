# Problem 36
from typing import List


class ValidSudoku:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        flags = [[[True for k in range(len(board))] for c in range(len(board))] for r in range(len(board))]

        for r in range(len(board)):
            for c in range(len(board)):
                if board[r][c] != ".":
                    val = ord(board[r][c]) - ord('1')
                    if not flags[r][c][val]:
                        return False
                    for r1 in range(len(board)):
                        flags[r1][c][val] = False
                    for c1 in range(len(board)):
                        flags[r][c1][val] = False

                    rq, cq = r // 3, c // 3
                    for dr in range(3):
                        for dc in range(3):
                            rr, cc = rq * 3 + dr, cq * 3 + dc
                            flags[rr][cc][val] = False

        for r in range(len(board)):
            for c in range(len(board)):
                if board[r][c] == ".":
                    flag = False
                    for val in range(1, 10, 1):
                        for r1 in range(len(board)):
                            if flags[r1][c][val]:
                                flag = True
                                break
                        if flag:
                            break

                        for c1 in range(len(board)):
                            if flags[r][c1][val]:
                                flag = True
                                break
                        if flag:
                            break

                        rq, cq = r // 3, c // 3
                        for dr in range(3):
                            for dc in range(3):
                                rr, cc = rq * 3 + dr, cq * 3 + dc
                                if flags[rr][cc][val]:
                                    flag = True
                                    break
                        if flag:
                            break
                    if not flag:
                        return False

        return True


if __name__ == '__main__':
    v = ValidSudoku()
    print(v.isValidSudoku(
        [["5", "3", ".", ".", "7", ".", ".", ".", "."]
            , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
            , [".", "9", "8", ".", ".", ".", ".", "6", "."]
            , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
            , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
            , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
            , [".", "6", ".", ".", ".", ".", "2", "8", "."]
            , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
            , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))
    print(v.isValidSudoku(
        [["8", "3", ".", ".", "7", ".", ".", ".", "."]
            , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
            , [".", "9", "8", ".", ".", ".", ".", "6", "."]
            , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
            , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
            , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
            , [".", "6", ".", ".", ".", ".", "2", "8", "."]
            , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
            , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    ))
