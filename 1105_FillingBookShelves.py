# Problem 1105
from typing import List


class FillingBookShelves:
    # I could not solve this
    # I peeked into the solution

    def minHeightShelves2(self, books: List[List[int]], shelfWidth: int) -> int:
        # books[1] = [width1, height1]
        memo = {0: 0, 1: books[0][1]}

        for i in range(2, len(books) + 1):
            # new shelf
            dp_i = books[i - 1][1] + memo[i - 1]

            # old shelf
            remain = shelfWidth - books[i - 1][0]
            max_height = books[i - 1][1]
            j = i - 1
            while remain - books[j - 1][0] >= 0 and j > 0:
                # dp[i] is dependent on dp[i-1] ,, and so on
                # till remain >= 0
                # dp[i] = dp[j] + max(heights[j:i+1])
                # only till j is in present shelf
                max_height = max(max_height, books[j - 1][1])
                # j - 1 th book is in a different (below) shelf
                dp_i = min(dp_i, memo[j - 1] + max_height)
                remain = remain - books[j - 1][0]
                j -= 1
            memo[i] = dp_i
        return memo[len(books)]


if __name__ == '__main__':
    f = FillingBookShelves()
    print(f.minHeightShelves([[1, 3], [2, 4], [3, 2]], 6))
    # 4
    print(f.minHeightShelves([[1, 1], [2, 3], [2, 3], [1, 1], [1, 1], [1, 1], [1, 2]], 4))
    # 6
