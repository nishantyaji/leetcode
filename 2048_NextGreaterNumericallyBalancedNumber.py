# Problem 2048
import bisect
import functools


class NextGreaterNumericallyBalancedNumber:
    def nextBeautifulNumber(self, n: int) -> int:

        univ = self.get_universe()
        print(univ)
        r = bisect.bisect_right(univ, n)
        return univ[r]

    @functools.cache
    def get_universe(self):
        return self.sixer()

    def sixer(self):
        universe = [155555, 515555, 551555, 555155, 555515, 555551, 666666]
        base = 444444
        for i in range(0, 5):
            for j in range(i + 1, 6):
                temp = base + ((-2) * (pow(10, i) + pow(10, j)))
                universe += [temp]

        base = 333333
        for i in range(0, 4):
            for j in range(i + 1, 5):
                for k in range(j + 1, 6):
                    for l in range(3):

                        if l == 0:
                            o, a, b = i, j, k
                        elif l == 1:
                            o, a, b = j, i, k
                        else:
                            o, a, b = k, i, j
                        temp = base + ((-2) * pow(10, o) - pow(10, a) - pow(10, b))
                        universe += [temp]

        universe += [55555, 14444, 41444, 44144, 44414, 44441, 22333, 23233, 23323, 23332,
                     32233, 32323, 32332, 33223, 33232, 33322]

        universe += [4444, 1333, 3133, 3313, 3331, 333, 122, 212, 221, 1, 22]

        universe += [1224444]
        return list(sorted(set(universe)))
