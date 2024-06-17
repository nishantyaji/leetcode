# Problem 733

from typing import List


class FloodFill:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        prev_color = image[sr][sc]
        if prev_color == color:
            return image

        q = []
        rows, cols = len(image), len(image[0])

        def color_and_ret_neighbours(r: int, c: int, color: int):
            neighbours = []
            if r > 0 and image[r - 1][c] == prev_color:
                image[r - 1][c] = color
                neighbours.append([r - 1, c])
            if c > 0 and image[r][c - 1] == prev_color:
                image[r][c - 1] = color
                neighbours.append([r, c - 1])
            if r < rows - 1 and image[r + 1][c] == prev_color:
                image[r + 1][c] = color
                neighbours.append([r + 1, c])
            if c < cols - 1 and image[r][c + 1] == prev_color:
                image[r][c + 1] = color
                neighbours.append([r, c + 1])

            return neighbours

        mylist = [[sr, sc]]
        image[sr][sc] = color

        while len(mylist) > 0:
            neighbours = color_and_ret_neighbours(mylist[0][0], mylist[0][1], color)
            del mylist[0]
            mylist = mylist + neighbours

        return image


if __name__ == '__main__':
    f = FloodFill()
    print(f.floodFill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2))
    print(f.floodFill([[0, 0, 0], [0, 0, 0]], 0, 0, 0))
