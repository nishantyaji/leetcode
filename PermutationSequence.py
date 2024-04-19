# Problem 60

class PermutationSequence:
    def getPermutation(self, n: int, k: int) -> str:
        fact_dict = {0: 1, 1: 1}
        for i in range(2, n):
            fact_dict[i] = i * fact_dict[i - 1]
        chars = [str(x) for x in range(1, n + 1)]
        result = ""
        k -= 1
        while n >= 1:
            q, r = int(k / fact_dict[n - 1]), k % fact_dict[n - 1]
            result += chars[q]
            del chars[q]
            k, n = r, n - 1
        return result


if __name__ == '__main__':
    p = PermutationSequence()
    print(p.getPermutation(4, 6))  # 1432
    print(p.getPermutation(3, 2))  # 132
    print(p.getPermutation(3, 3))  # 213
    print(p.getPermutation(4, 9))  # 2314
    print(p.getPermutation(3, 1))  # 123
