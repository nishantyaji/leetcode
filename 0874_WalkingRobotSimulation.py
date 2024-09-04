# Problem 0874
import collections
import copy
from typing import List


class WalkingRobotSimulation:

    """
    Recommend Binary search solution shared here:
    https://leetcode.com/problems/walking-robot-simulation/solutions/5736137/binary-search-for-finding-obstacles/?envType=daily-question&envId=2024-09-04
    """

    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        turnd = collections.defaultdict(dict)
        turnd[(0, 1)][-2] = -1, 0
        turnd[(0, 1)][-1] = 1, 0
        turnd[(0, -1)][-2] = 1, 0
        turnd[(0, -1)][-1] = -1, 0
        turnd[(1, 0)][-2] = 0, 1
        turnd[(1, 0)][-1] = 0, -1
        turnd[(-1, 0)][-2] = 0, -1
        turnd[(-1, 0)][-1] = 0, 1

        def turn(val: int, dir: tuple) -> tuple:
            return turnd[dir][val]

        obsset = set()
        for obs in obstacles:
            if obs:
                obsset.add((obs[0], obs[1]))

        def move(pres: tuple, dir: tuple, val: int):
            x, y = copy.deepcopy(pres)
            if dir[0] != 0:
                if dir[0] < 0:
                    # instead of a linear scan
                    # we can use a binary search
                    for _ in range(val):
                        if (x - 1, y) in obsset:
                            return x, y
                        x -= 1
                else:
                    # instead of a linear scan
                    # we can use a binary search
                    for _ in range(val):
                        if (x + 1, y) in obsset:
                            return x, y
                        x += 1
            else:
                if dir[1] < 0:
                    # instead of a linear scan
                    # we can use a binary search
                    for _ in range(val):
                        if (x, y - 1) in obsset:
                            return x, y
                        y -= 1
                else:
                    # instead of a linear scan
                    # we can use a binary search
                    for _ in range(val):
                        if (x, y + 1) in obsset:
                            return x, y
                        y += 1
            return x, y

        direction = (0, 1)
        run_x, run_y = 0, 0
        max_ = 0
        for c in commands:
            if c < 0:
                direction = turn(c, direction)
            else:
                run_x, run_y = move((run_x, run_y), direction, c)
                max_ = max(max_, (run_x * run_x) + (run_y * run_y))

        return max_


if __name__ == '__main__':
    w = WalkingRobotSimulation()
    print(w.robotSim([7, -2, -2, 7, 5],
                     [[-3, 2], [-2, 1], [0, 1], [-2, 4], [-1, 0], [-2, -3], [0, -3], [4, 4], [-3, 3], [2, 2]]))
    print(w.robotSim([4, -1, 3], [[]]))  # 25
    print(w.robotSim([4, -1, 4, -2, 4], [[2, 4]]))  # 65
    print(w.robotSim([6, -1, -1, 6], [[]]))  # 36
