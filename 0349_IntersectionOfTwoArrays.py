#Problem 349
from typing import List

class IntersectionOfTwoArrays:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mySet = set(nums1)
        returnSet = set()
        for i in nums2:
            if i in mySet:
                returnSet.add(i)
                
        return list(returnSet)
    
    
if __name__ == '__main__':
    i = IntersectionOfTwoArrays()
    print(i.intersection( [1,2,2,1], [2,2]))
    print(i.intersection([4,9,5], [9,4,9,8,4]))