# Problem 2017
import itertools
import sys
from typing import List


class GridGame:
    def gridGame(self, grid: List[List[int]]) -> int:
        cols = len(grid[0])
        """
        After the first robot goes through
        the second robot has to pick up the rest
        
        Note that after the first robot goes through
        there are no columns where both the rows are non-zeroes
        This is because the first robot visits all columns atleast once
        and hoovers up the value
        
        In the first row once you get a non zero item you are sure that 
        the values to the right are non zero
        In the second row once you get a zero item you are sure that 
        what follows are zeros
        Note that when the first row is zero the second row is non zero 
        and vice versa
        
        The optimum method is to consume all in a single row before the end
        """
        suffix_0 = list(itertools.accumulate(grid[0][::-1]))[::-1][1:] + [0]
        prefix_1 = [0] + list(itertools.accumulate(grid[1]))[:-1]
        res = sys.maxsize
        for idx in range(0, cols):
            local_max = max(prefix_1[idx], suffix_0[idx])
            res = min(res, local_max)
        return res


if __name__ == '__main__':
    g = GridGame()
    print(g.gridGame([[2, 5, 4], [1, 5, 1]]))  # 4
    print(g.gridGame([[3, 3, 1], [8, 5, 2]]))  # 4
    print(g.gridGame([[1, 3, 1, 15], [1, 3, 3, 1]]))  # 7
