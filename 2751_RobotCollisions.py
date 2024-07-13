# Problem 2751
import operator
from typing import List


class RobotCollisions:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        stack, quads = [], list(zip(positions, healths, directions, list(range(len(positions)))))
        quads.sort(key=operator.itemgetter(0))
        for i in range(len(quads)):
            popped, count, collision, recent = False, 0, False, quads[i]
            while stack and stack[-1][2] == "R" and recent[2] == "L":
                collision, popped, top = True, False, stack.pop()
                count += 1
                if top[1] > recent[1]:
                    stack.append((top[0], top[1] - 1, top[2], top[3]))
                    break
                elif top[1] < recent[1]:
                    popped = True
                else:
                    break
                recent = (recent[0], recent[1] - 1, recent[2], recent[3])

            if collision:
                if popped:
                    stack.append(recent)
            else:
                stack.append(quads[i])
        stack.sort(key=operator.itemgetter(3))
        return list(map(lambda x: x[1], stack))


if __name__ == '__main__':
    r = RobotCollisions()
    print(r.survivedRobotsHealths([3, 2, 30, 24, 38, 7], [47, 12, 49, 11, 47, 38], "RRLRRR"))
    # [12, 47]
    print(r.survivedRobotsHealths([11, 44, 16], [1, 20, 17], "RLR"))
    # [18]
    print(r.survivedRobotsHealths([5, 4, 3, 2, 1], [2, 17, 9, 15, 10], "RRRRR"))
    # [2,17,9,15,10]
    print(r.survivedRobotsHealths([3, 5, 2, 6], [10, 10, 15, 12], "RLRL"))
    # [14]
    print(r.survivedRobotsHealths([1, 2, 5, 6], [10, 10, 11, 11], "RLRL"))
    # []
