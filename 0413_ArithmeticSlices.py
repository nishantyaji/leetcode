# problem 413
from typing import List

class ArithmeticSlices:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return 0
        diff = None
        count = 0
        result = 0
        
        for i in range(1, len(nums)):
            if diff != nums[i] - nums[i-1]:
                if count >= 2:
                    result = result + (int) ((count+2)* (count + 1) /2 ) - (2 * (count +1)- 1)
                count = 1
                diff = nums[i] - nums[i-1]
            else:
                count = count + 1
                
        if count >= 2:
            result = result + (int) ((count+2) * (count + 1) /2 ) - (2 * (count+1) - 1)

        return result

    
if __name__ == "__main__":
    a = ArithmeticSlices()
    print(a.numberOfArithmeticSlices([1, 2, 3]))
    print(a.numberOfArithmeticSlices([1,2,3,4]))
    print(a.numberOfArithmeticSlices([1]))
    