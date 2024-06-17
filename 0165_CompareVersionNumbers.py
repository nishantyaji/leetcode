#Problem 165

class CompareVersionNumbers:
    def compareVersion(self, version1: str, version2: str) -> int:
        tokens1 = version1.split(".")
        tokens2 = version2.split(".")
        ints1 = [int(x) for x in tokens1]
        ints2 = [int(x) for x in tokens2]
        common_len = min(len(ints1), len(ints2))
        for i in range(0, common_len):
            if ints1[i] > ints2[i]:
                return 1
            elif ints2[i] > ints1[i]:
                return -1

        rem1 = len(ints1) - common_len
        rem2 = len(ints2) - common_len

        if rem1 > 0 and sum(ints1[common_len:]) > 0:
            return 1

        if rem2 > 0 and sum(ints2[common_len:]) > 0:
            return -1
        return 0