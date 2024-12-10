# Problem 2982
import collections


class FindLongestSpecialStringThatOccursThriceI:
    def maximumLength(self, s: str) -> int:
        cntr_list = [collections.defaultdict(int) for _ in range(len(s) + 1)]
        prev, count = "~", 1
        for c in s:
            if c == prev:
                count += 1
                continue
            if prev != "~":
                for cnt in range(count, 0, -1):
                    cntr_list[cnt][prev] += (count + 1 - cnt)
            prev, count = c, 1

        for cnt in range(count, 0, -1):
            cntr_list[cnt][prev] += (count + 1 - cnt)

        for i, mp in enumerate(cntr_list[::-1]):
            for k, v in mp.items():
                if v > 2:
                    return len(s) - i
        return -1


if __name__ == '__main__':
    f = FindLongestSpecialStringThatOccursThriceI()
    print(f.maximumLength("aaaa"))  # 2
    print(f.maximumLength("abcdef"))  # -1
    print(f.maximumLength("abcaba"))  # 1
