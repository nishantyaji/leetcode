# Problem 3146
class PermutationDiffBetweenTwoStrings:
    def findPermutationDifference(self, s: str, t: str) -> int:
        res_list = [0] * 26

        for i in range(0, len(s)):
            chs = s[i]
            cht = t[i]
            orda = ord('a')
            res_list[ord(s[i]) - orda] = res_list[ord(s[i]) - orda] + i
            res_list[ord(t[i]) - orda] = res_list[ord(t[i]) - orda] - i

        sum_all = 0
        for i in range(0, len(res_list)):
            sum_all += abs(res_list[i])

        return sum_all


if __name__ == '__main__':
    w = PermutationDiffBetweenTwoStrings()
    print(w.findPermutationDifference("abc", "bac"))
    print(w.findPermutationDifference("abcde", "edbac"))
