# Problem 1653


class MinDeletionsToMakeStringBalanced:
    def minimumDeletions(self, s: str) -> int:
        total_a = 0
        total_b = 0
        b_left_list = []
        a_right_list = []
        for ch in s:
            b_left_list.append(total_b)
            a_right_list.append(-total_a)
            if ch == 'a':
                total_a = total_a + 1
            else:
                total_b = total_b + 1
        b_left_list.append(total_b)
        a_right_list.append(-total_a)

        min = len(s) + 2
        for i in range(0, len(s) + 1):
            temp = b_left_list[i] + a_right_list[i] + total_a
            if temp < min:
                min = temp
        return min


if __name__ == '__main__':
    m = MinDeletionsToMakeStringBalanced()
    print(m.minimumDeletions("a"))
    print(m.minimumDeletions("aababbab"))
    print(m.minimumDeletions("bbaaaaabb"))
