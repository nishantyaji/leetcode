# Problem 2147

class NumWaysToDivideALongCorridor:
    def numberOfWays(self, corridor: str) -> int:
        res = 1
        scount = 0
        pcount = 0
        count = sum([1 if x == 'S' else 0 for x in corridor])
        if count < 1 or count % 2 == 1:
            return 0
        for c in corridor:
            if scount == 2:
                if c == 'P':
                    pcount += 1
                else:
                    res *= (pcount + 1)
                    pcount = 0
                    scount = 1
            else:
                if c == 'S':
                    scount += 1
                    pcount = 0
                else:
                    pass
        return res % 1000000007
