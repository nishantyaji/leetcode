# Problem 763
import collections
from typing import List


class PartitionLabels:

    def partitionLabels(self, s: str) -> List[int]:
        d = collections.defaultdict(list)
        for i, c in enumerate(s):
            d[c].append(i)

        i, cnt, last, last_idx = 0, 0, {}, 0

        while True:
            while i < len(s) and i <= last_idx:
                last_idx = max(d[s[i]][-1], last_idx)
                last[cnt] = last_idx
                i += 1
            if i >= len(s):
                break
            last_idx = i
            cnt += 1

        if last[cnt] != len(s) - 1:
            cnt += 1
            last[cnt] = len(s) - 1

        res = [last[0] + 1]
        for i in range(1, cnt + 1):
            res.append(last[i] - last[i-1])

        return res


if __name__ == '__main__':
    p = PartitionLabels()
    print(p.partitionLabels("ababcbacadefegdehijhklij"))
    print(p.partitionLabels("eccbbbbdec"))
