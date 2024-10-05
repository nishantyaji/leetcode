# Problem 567
import collections


class PermutationString:

    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        cntr = collections.Counter(s1)
        my_dict = collections.Counter(s2[:len(s1)])
        if self.cntr_equals(cntr, my_dict):
            return True

        for i in range(1, len(s2) - len(s1) + 1):
            my_dict[s2[i - 1]] -= 1
            if my_dict[s2[i - 1]] == 0:
                del my_dict[s2[i - 1]]
            my_dict[s2[i + len(s1) - 1]] += 1
            if self.cntr_equals(cntr, my_dict):
                return True

        return False

    def cntr_equals(self, c1: dict, c2: dict):
        if len(c1) != len(c2):
            return False

        for k, v in c1.items():
            if c2[k] != v:
                return False
        return True


if __name__ == '__main__':
    p = PermutationString()
    print(p.checkInclusion("ab", "eidbaooo"))
    print(p.checkInclusion("ab", "eidboaoo"))
