# Problem 1931
import collections
import functools


class PaintingAGridWith3DifferentColors:

    @functools.cache
    def calculate(self, m: int):
        poss = [i for i in range(pow(3, m)) if not self.self_lap(i, m)]
        adj = collections.defaultdict(list)
        for p in poss:
            for q in poss:
                if not self.overlaps(p, q, m):
                    adj[p].append(q)

        cntr = collections.Counter([len(v) for _, v in adj.items()])
        return adj

    def overlaps(self, a: int, b: int, m: int) -> bool:
        a_str, b_str = self.base3(a, m), self.base3(b, m)
        for k in range(m):
            if a_str[k] == b_str[k]:
                return True
        return False

    def self_lap(self, a: int, m: int):
        a_str = self.base3(a, m)
        for i in range(len(a_str) - 1):
            if a_str[i] == a_str[i+1]:
                return True
        return False


    def base3(self, numm: int, m: int) -> str:
        res = list("".join(["0"] * m))
        i = m - 1
        while numm > 0:
            numm, r = divmod(numm, 3)
            res[i] = str(r)
            i -= 1
        return "".join(res)

    def recurse(self, m: int, n: int) -> dict:
        base = 1000000007
        adj = self.calculate(m)

        if n > 1:
            temp_1 = self.recurse(m, n - 1)
            temp = collections.Counter()
            for key, val in temp_1.items():
                for nei in adj[key]:
                    temp[nei] = (temp[nei] + val) % base
            return temp
        else:
            return {x: 1 for x in adj.keys()}


    def colorTheGrid(self, m: int, n: int) -> int:
        base = 1000000007
        temp = self.recurse(m, n)
        return sum(temp.values()) % base


if __name__ == '__main__':
    p = PaintingAGridWith3DifferentColors()
    print(p.colorTheGrid(1, 1))
    print(p.colorTheGrid(1, 2))
    print(p.colorTheGrid(5, 5))
