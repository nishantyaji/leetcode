# Problem 1992

from typing import List


class FindAllGroupOfFarmland:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        visited = 2
        farm = 1
        rows, cols = len(land), len(land[0])
        result = []
        for r in range(0, rows):
            for c in range(0, cols):
                if land[r][c] == farm:
                    temp_r, temp_c = r, c
                    while temp_c < cols and land[temp_r][temp_c] == farm:
                        temp_c += 1
                    temp_c -= 1
                    while temp_r < rows and land[temp_r][temp_c] == farm:
                        temp_r += 1
                    temp_r -= 1
                    result.append([r, c, temp_r, temp_c])
                    for x in range(r, temp_r + 1):
                        for y in range(c, temp_c + 1):
                            land[x][y] = visited
        return result


if __name__ == '__main__':
    f = FindAllGroupOfFarmland()
    print(f.findFarmland([[1, 0, 0], [0, 1, 1], [0, 1, 1]]))
    print(f.findFarmland([[1, 1], [1, 1]]))
    print(f.findFarmland([[0]]))
