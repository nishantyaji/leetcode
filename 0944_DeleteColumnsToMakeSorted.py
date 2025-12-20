# Problem 944
from typing import List


class DeleteColumnsToMakeSorted:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0
        for i in range(len(strs[0])):
            prev = ord('a') - 1
            for s in strs:
                if ord(s[i]) - prev < 0:
                    count += 1
                    break
                prev = ord(s[i])
        return count
