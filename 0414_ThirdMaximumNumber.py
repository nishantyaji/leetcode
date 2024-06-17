# Problem 414
from typing import List
class Util:
    def __init__(self):
        self.largest = None
        self.secondlargest = None
        self.thirdlargest = None
        
    def addnum(self, num: int):
        if num == self.largest or num == self.secondlargest or num == self.thirdlargest:
            return 
        if self.largest is None:
            self.largest = num
        elif self.secondlargest is None and num < self.largest:
            self.secondlargest = num
        elif self.thirdlargest is None and (self.secondlargest is not None and num < self.secondlargest):
            self.thirdlargest = num
        else:
            if self.thirdlargest is not None and num < self.thirdlargest:
                pass
            else:
                if num > self.largest:
                    self.thirdlargest = self.secondlargest
                    self.secondlargest = self.largest
                    self.largest = num
                elif num < self.secondlargest:
                    self.thirdlargest = num
                elif num > self.secondlargest and num < self.largest:
                    self.thirdlargest = self.secondlargest
                    self.secondlargest = num
                else:
                    pass
                    

class ThirdMaximumNumber:
    def thirdMax(self, nums: List[int]) -> int:
        u = Util()
        for num in nums:
            u.addnum(num)
        return u.thirdlargest if u.thirdlargest is not None else u.largest
        
    
if __name__ == "__main__":
    t = ThirdMaximumNumber()
    print(t.thirdMax([1,2]))
    print(t.thirdMax([3,2,1]))
    print(t.thirdMax([2,2,3,1]))


    