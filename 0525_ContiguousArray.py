#Problem 525

from typing import List

class ContiguousArray:
    def findMaxLength(self, nums: List[int]) -> int:
        
        parity = 0
        mydict = {0: -1}
        this_max = 0
        for i in range(0, len(nums)):
            if nums[i] == 0:
                parity -=1
            else:
                parity += 1

            if i > 0 and parity in mydict:
                first_idx = mydict[parity]
                diff = i - first_idx
                if diff > this_max:
                    this_max = diff
            else:
                mydict[parity] = i
                
        return this_max
        
            
if __name__ == '__main__':
    c = ContiguousArray()
    print(c.findMaxLength([0,1]))
    print(c.findMaxLength([0,1, 0]))
    print(c.findMaxLength([0,0,0,1,1,1,0]))