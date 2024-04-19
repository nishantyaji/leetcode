#Problem 130

from typing import List


class SurroundedRegions:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        visited = '1'
        isle = 'O'
        cross = 'X'
        rows, cols = len(board), len(board[0])

        def get_neighbours(r: int, c: int):
            neighbours = []
            if r > 0 and board[r - 1][c] == isle:
                board[r - 1][c] = visited
                neighbours.append([r - 1, c])
            if c > 0 and board[r][c - 1] == isle:
                board[r][c - 1] = visited
                neighbours.append([r, c - 1])
            if r < rows - 1 and board[r + 1][c] == isle:
                board[r + 1][c] = visited
                neighbours.append([r + 1, c])
            if c < cols - 1 and board[r][c + 1] == isle:
                board[r][c + 1] = visited
                neighbours.append([r, c + 1])
            return neighbours

        for row in [0, rows - 1]:
            for col in range(0, cols):
                if board[row][col] == isle:
                    eval_list = [[row, col]]
                    board[row][col] = visited
                    while len(eval_list) > 0:
                        [temp_row, temp_col] = eval_list[0]
                        neighbours = get_neighbours(temp_row, temp_col)
                        del eval_list[0]
                        eval_list += neighbours

        for row in range(0, rows):
            for col in [0, cols - 1]:
                if board[row][col] == isle:
                    eval_list = [[row, col]]
                    board[row][col] = visited
                    while len(eval_list) > 0:
                        [temp_row, temp_col] = eval_list[0]
                        neighbours = get_neighbours(temp_row, temp_col)
                        del eval_list[0]
                        eval_list += neighbours

        for row in range(0, rows):
            for col in range(0, cols):
                if board[row][col] == isle:
                    board[row][col] = cross

        for row in range(0, rows):
            for col in range(0, cols):
                if board[row][col] == visited:
                    board[row][col] = isle


if __name__ == '__main__':
    s = SurroundedRegions()
    s.solve([["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]])
    s.solve([["X", "O", "O", "X", "X", "X", "O", "X", "O", "O"], ["X", "O", "X", "X", "X", "X", "X", "X", "X", "X"],
             ["X", "X", "X", "X", "O", "X", "X", "X", "X", "X"], ["X", "O", "X", "X", "X", "O", "X", "X", "X", "O"],
             ["O", "X", "X", "X", "O", "X", "O", "X", "O", "X"], ["X", "X", "O", "X", "X", "O", "O", "X", "X", "X"],
             ["O", "X", "X", "O", "O", "X", "O", "X", "X", "O"], ["O", "X", "X", "X", "X", "X", "O", "X", "X", "X"],
             ["X", "O", "O", "X", "X", "O", "X", "X", "O", "O"], ["X", "X", "X", "O", "O", "X", "O", "X", "X", "O"]])
