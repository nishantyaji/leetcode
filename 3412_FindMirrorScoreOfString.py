# Problem 3412
import collections


class FindMirrorScoreOfString:
    def calculateScore(self, s: str) -> int:
        alpha = "abcdefghijklmnopqrstuvwxyz"
        mp = {x: alpha[25 - i] for i, x in enumerate(alpha)}
        cntr = collections.defaultdict(list)
        score = 0
        for i in range(len(s)):
            if len(cntr[mp[s[i]]]) > 0:
                temp = cntr[mp[s[i]]].pop()
                score += (i - temp)
            else:
                cntr[s[i]].append(i)
        return score
