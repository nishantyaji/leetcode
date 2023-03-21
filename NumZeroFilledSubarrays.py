# Problem 2348
from typing import List

class NumZeroFilledSubarrays:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
       
        is_prev_zero = False
        zero_count = 0
        result = 0
        
        for num in nums:
            if num == 0:
                if is_prev_zero == True:
                    zero_count = zero_count + 1
                else:
                    zero_count = 1
                    is_prev_zero = True
            else:
                if is_prev_zero == True:
                    result = result + (int) (zero_count * (zero_count + 1)/2)
                is_prev_zero = False
                zero_count = 0
                
        if is_prev_zero == True:
            result = result + (int) (zero_count * (zero_count + 1)/2)

        return result

            
if __name__ == "__main__":
    n = NumZeroFilledSubarrays()
    print(n.zeroFilledSubarray([1,3,0,0,2,0,0,4]))
    print(n.zeroFilledSubarray([0,0,0,2,0,0]))
    print(n.zeroFilledSubarray([2,10,2019]))