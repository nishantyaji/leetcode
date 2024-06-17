#Problem 442
from typing import List


class FindAllDuplicatesInAnArray:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        mylist = []
        for i in range(1, len(nums) + 1):
            mylist.append(i)
        myset = set(mylist)

        result = []
        for i in nums:
            if i in myset:
                myset.remove(i)
            else:
                result.append(i)

        return result

if __name__ == '__main__':
    f = FindAllDuplicatesInAnArray()
    print(f.findDuplicates([4,3,2,7,8,2,3,1]))