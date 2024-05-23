# Problem 2597
import collections
from typing import List


class NumOfBeautifulSubsets:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        index_map, nums_dict = collections.defaultdict(list), collections.defaultdict(list)
        for idx, num in enumerate(nums):
            index_map[num].append(idx)
        for num in nums:
            if num + k in index_map:
                for idx in index_map[num]:
                    nums_dict[idx] = index_map[num+k]
        del index_map
        result = 0
        for i in range(1, pow(2, len(nums))):
            flags = list(bin(i)[2:].rjust(len(nums), '0'))
            skip = False
            for k, values in nums_dict.items():
                for v in values:
                    if flags[k] == flags[v] and flags[k] == '1':
                        skip = True
                        break
                if skip:
                    break
            if not skip:
                result += 1
        return result


if __name__ == '__main__':
    n = NumOfBeautifulSubsets()
    print(n.beautifulSubsets([1,2,3,3], 1))
    #8
    print(n.beautifulSubsets([2, 4, 6], 2))
    print(n.beautifulSubsets([1], 1))
