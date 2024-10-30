# Problem 1411

import collections


class NumWaysPaintNX3Grid:
    def numOfWays(self, n: int) -> int:
        base = 1000000007
        # self.calculate()  # uncomment this line to understand parity
        res = [(0, 0), (6, 6), (24, 30)]
        for i in range(3, 5001):
            fours = res[i - 1][0] * 2
            fives = res[i - 1][0] * 2
            fours += res[i - 1][1] * 2
            fives += res[i - 1][1] * 3
            res.append((fours % base, fives % base))
        return (res[n][0] + res[n][1]) % base

    def calculate(self):
        poss = [i for i in range(27) if not self.self_lap(i)]
        adj = collections.defaultdict(list)
        for p in poss:
            for q in poss:
                if not self.overlaps(p, q):
                    adj[p].append(q)

        for k, v in adj.items():
            v = " , ".join(list(map(lambda x: x.rjust(2, "0"), map(str, v))))
            print(str(k).rjust(2, "0"), " = ", v)
        print(adj)

    def overlaps(self, a: int, b: int) -> bool:
        a_str, b_str = self.base3(a), self.base3(b)
        for k in range(3):
            if a_str[k] == b_str[k]:
                return True
        return False

    def self_lap(self, a: int):
        a_str = self.base3(a)
        return a_str[1] == a_str[0] or a_str[2] == a_str[1]

    def base3(self, numm: int) -> str:
        res = list("000")
        i = 2
        while numm > 0:
            numm, r = divmod(numm, 3)
            res[i] = str(r)
            i -= 1
        return "".join(res)


if __name__ == '__main__':
    n = NumWaysPaintNX3Grid()
    print(n.numOfWays(5000))  # 30228214
