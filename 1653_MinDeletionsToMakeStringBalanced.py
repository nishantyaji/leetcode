# Problem 1653


class MinDeletionsToMakeStringBalanced:
    def minimumDeletions(self, s: str) -> int:
        total_a = 0
        total_b = 0
        min = 1e6
        for ch in s:
            temp = total_b - total_a
            if temp < min:
                min = temp
            if ch == 'a':
                total_a = total_a + 1
            else:
                total_b = total_b + 1
        if total_b  - total_a < min:
            min = total_b - total_a

        return min + total_a


if __name__ == '__main__':
    m = MinDeletionsToMakeStringBalanced()
    print(m.minimumDeletions("a"))
    print(m.minimumDeletions("aababbab"))
    print(m.minimumDeletions("bbaaaaabb"))
