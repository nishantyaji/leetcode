# Problem 3175. Find The First Player to win K Games in a Row
from typing import List


class FindFirstPlayerToWinKGamesInRow:
    def findWinningPlayer(self, skills: List[int], k: int) -> int:
        if k > len(skills):
            this_max, this_index = 0, -1
            for i, s in enumerate(skills):
                if s > this_max:
                    this_max, this_index = s, i
            return this_index
        new_skills = skills + skills
        this_max, this_idx, run_max = 0, -1, 0
        for idx, s in enumerate(new_skills):
            if s > this_max:
                this_max = s
                this_index = idx % len(skills)
                run_max = 1 if idx != 0 else 0
            else:
                run_max += 1
            if run_max >= k:
                return this_index


if __name__ == '__main__':
    b = FindFirstPlayerToWinKGamesInRow()
    print(b.findWinningPlayer([1, 6, 17], 1))
    print(b.findWinningPlayer([16, 4, 7, 17], 562084119))
    print(b.findWinningPlayer([4, 2, 6, 3, 9], 2))
    print(b.findWinningPlayer([2, 5, 4], 3))
