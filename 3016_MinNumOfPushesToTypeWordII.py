# Problem 3016
import collections
import operator


class MinNumOfPushesToTypeWordII:
    def minimumPushes(self, word: str) -> int:
        cntr = collections.Counter(word)
        tuples = [(k, v) for k, v in cntr.items()]
        tuples.sort(key=operator.itemgetter(1), reverse=True)
        q = ([1] * 8) + ([2] * 8) + ([3] * 8) + ([4] * 2)
        zipr = zip(map(lambda t: t[1], tuples), q[:len(tuples)])
        return sum(list(map(lambda z: z[0] * z[1], zipr)))


if __name__ == '__main__':
    m = MinNumOfPushesToTypeWordII()
    print(m.minimumPushes("abcde"))
    print(m.minimumPushes("xyzxyzxyzxyz"))
    print(m.minimumPushes("aabbccddeeffgghhiiiiii"))
