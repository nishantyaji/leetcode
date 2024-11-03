from typing import List


class BinaryLifting:

    # Implementation of binary lifting (jump pointers)

    def __init__(self, n: int, parent: List[int]):
        self.parent = parent
        limit = n.bit_length() + 1
        sz = len(self.parent)
        self.dp = [[-1 for c in range(limit)] for r in range(sz)]

        for i in range(sz):
            self.dp[i][0] = self.parent[i]

        for j in range(1, limit):
            # Find first parent in the first outer loop
            # and then the grandparent
            # This is done so that the changing the for loops does not work
            # if parent of 1 is 4 then dp[1][2] = dp[dp[1][1]][1] = dp[4][1] = -1
            # because with the change in for-loops dp[4] is not yet computed
            for i in range(sz):
                if self.dp[i][j - 1] == -1:
                    self.dp[i][j] = -1
                else:
                    self.dp[i][j] = self.dp[self.dp[i][j - 1]][j - 1]

    def getKthAncestor(self, node: int, k: int) -> int:
        if k > len(self.dp[0]):
            return -1
        bin_k = list(map(int, list(bin(k)[2:])))
        base = 1
        for i in bin_k[::-1]:
            if i == 1:
                node = self.dp[node][base - 1]
                if node == -1:
                    return -1
            base += 1
        return node
