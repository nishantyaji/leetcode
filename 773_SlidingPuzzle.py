# Problem 773
import copy
from typing import List


class SlidingPuzzle:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        board_str = "".join(list(map(str, board[0] + board[1])))

        def adj(rr, cc):
            adjset = {(1 - rr, cc)}
            if cc != 2:
                adjset.add((rr, 1 + cc))
            if cc != 0:
                adjset.add((rr, cc - 1))
            return adjset

        """
        Leet code hint
        Perform a breadth-first-search, where the nodes are the puzzle boards
         and edges are if two puzzle boards can be transformed 
         into one another with one move.
         
         I was trying to find tactics (a la game-theory) in vain.
         I could crack the problem soon after looking up the hint
        """

        visited = set(board_str)
        zero_idx = board_str.find("0")
        r0, c0 = divmod(zero_idx, 3)
        q = [(board_str, (r0, c0), 0)]
        while q:
            board_str, (r, c), steps = q.pop()
            if board_str == "123450":
                return steps
            neis = adj(r, c)
            for (rn, cn) in neis:
                board_str_copy = list(copy.deepcopy(board_str))
                board_str_copy[3 * r + c] = board_str_copy[3 * rn + cn]
                board_str_copy[3 * rn + cn] = "0"
                board_str_copy = "".join(board_str_copy)
                if board_str_copy not in visited:
                    q = [(board_str_copy, (rn, cn), steps + 1)] + q
                    visited.add(board_str_copy)

        return -1


if __name__ == '__main__':
    s = SlidingPuzzle()
    print(s.slidingPuzzle([[4, 1, 2], [5, 0, 3]]))  # 5
    print(s.slidingPuzzle([[1, 2, 3], [4, 0, 5]]))  # 1
    print(s.slidingPuzzle([[1, 2, 3], [5, 4, 0]]))  # -1

