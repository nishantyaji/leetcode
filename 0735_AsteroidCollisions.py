# Problem 735
from typing import List


class AsteroidCollisions:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        # This is similar to problem 2751
        for i in range(len(asteroids)):
            popped, collision = False, False,
            while stack and stack[-1] * asteroids[i] < 0 < stack[-1]:
                collision, popped, top = True, False, stack.pop()
                if abs(top) > abs(asteroids[i]):
                    stack.append(top)
                    break
                elif abs(top) < abs(asteroids[i]):
                    popped = True
                else:
                    break

            if collision:
                if popped:
                    stack.append(asteroids[i])
            else:
                stack.append(asteroids[i])

        return stack


if __name__ == '__main__':
    a = AsteroidCollisions()
    print(a.asteroidCollision([5, 10, -5]))
    # [5, 10]
    print(a.asteroidCollision([8, -8]))
    # []
    print(a.asteroidCollision([10, 2, -5]))
    # [10]
