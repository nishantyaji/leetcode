# https://leetcode.com/problems/block-placement-queries/solutions/5207135/bit-sortedlist-reverse-temporal-order/

# or https://walkccc.me/LeetCode/problems/3161/#__tabbed_1_3

class BIT:
    def __init__(self, n):
        self.n = n
        self.l = [0] * (n + 1)
    def add(self, i, x):
        i += 1
        while i <= self.n:
            self.l[i] = max(x, self.l[i])
            i += i & -i
    def query(self, i):
        i += 1
        ans = 0
        while i:
            ans = max(ans, self.l[i])
            i -= i & -i
        return ans