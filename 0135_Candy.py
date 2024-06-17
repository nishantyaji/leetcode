# Problem 135

from typing import List


class Candy:
    def candy(self, ratings: List[int]) -> int:
        right_is_greater, left_is_greater = [False] * len(ratings), [False] * len(ratings)
        for i in range(len(ratings) - 1):
            left_is_greater[i] = ratings[i] > ratings[i + 1]
            right_is_greater[len(ratings) - i - 1] = ratings[len(ratings) - i - 2] < ratings[len(ratings) - i - 1]

        cum_left, cum_right = [0] * len(ratings), [0] * len(ratings)
        for i in range(len(ratings)):
            if right_is_greater[i]:
                cum_right[i] = cum_right[i - 1] + 1

        for i in range(len(ratings) - 1, -1, -1):
            if left_is_greater[i]:
                cum_left[i] = cum_left[i + 1] + 1

        result = [0] * len(ratings)
        for i in range(len(ratings)):
            result[i] = max(cum_left[i], cum_right[i]) + 1
        return sum(result)


if __name__ == '__main__':
    c = Candy()
    print(c.candy([1, 2, 87, 87, 87, 2, 1]))
    # 13

    print(c.candy([1, 0, 2]))
    print(c.candy([1, 2, 2]))
