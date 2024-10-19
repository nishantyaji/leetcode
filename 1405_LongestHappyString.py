# Problem 1405
import operator


class LongestHappyString:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        tuples = [[a, "a"], [b, "b"], [c, "c"]]
        res = ""
        while tuples:
            tuples.sort(key=operator.itemgetter(0), reverse=True)
            if len(tuples) == 1:
                i = 0
                while len(res) >= i + 1 and res[-1 - i] == tuples[0][1]:
                    i += 1
                res += "".join([tuples[0][1]] * max((min(2, tuples[0][0]) - i), 0))
                break

            high_remove = min(2, tuples[0][0])
            res += "".join([tuples[0][1]] * high_remove)

            mid_remove = min(1, tuples[1][0]) if tuples[0][0] > tuples[1][0] + 2 else min(2, tuples[1][0])
            res += "".join([tuples[1][1]] * mid_remove)

            high_count, mid_count, low_count = tuples[0][0] - high_remove, tuples[1][0] - mid_remove, tuples[2][
                0] if len(tuples) > 2 else 0
            new_tuples = []
            if high_count > 0:
                new_tuples.append((high_count, tuples[0][1]))
            if mid_count > 0:
                new_tuples.append((mid_count, tuples[1][1]))
            if low_count > 0:
                new_tuples.append((low_count, tuples[2][1]))
            tuples = new_tuples
        return res
