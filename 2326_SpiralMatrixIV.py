# Problem 2326
from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def get_from_array(arr: list[int]):
        orig = l = ListNode()
        for i, a in enumerate(arr):
            l.val = a
            if i != len(arr) - 1:
                l.next = ListNode()
            l = l.next
        return orig


class SpiralMatrixIV:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        visited = set()
        def exceeds(x, y, d):
            x_new, y_new = x + d[0], y + d[1]
            if 0 <= x_new < m and 0 <= y_new < n and (x_new, y_new) not in visited:
                return False
            return True

        dir_array = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        grid = [[-1 for c in range(n)] for r in range(m)]
        dir_idx, r, c = 0, 0, 0
        while head is not None:
            grid[r][c] = head.val
            visited.add((r, c))
            if exceeds(r, c, dir_array[dir_idx]):
                dir_idx = (dir_idx + 1) % 4
            r, c = r + dir_array[dir_idx][0], c + dir_array[dir_idx][1]
            head = head.next

        return grid


if __name__ == '__main__':
    s = SpiralMatrixIV()
    print(s.spiralMatrix(3, 5, ListNode.get_from_array([3, 0, 2, 6, 8, 1, 7, 9, 4, 2, 5, 5, 0])))
    print(s.spiralMatrix(1, 4, ListNode.get_from_array([0, 1, 2])))
