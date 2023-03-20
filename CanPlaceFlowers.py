# Problem 605

from typing import List


class CanPlaceFlowers:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        one_indices = []
        for i in range(0, len(flowerbed)):
            if flowerbed[i] == 1:
                one_indices.append(i)
                
        if len(one_indices) == 0:
            temp = (int) ((len(flowerbed) + 1) / 2)
            return temp >= n
                
        result = 0
        if flowerbed[0] == 0:
            temp = (int) (one_indices[0] / 2)
            result = result + temp
        for i in range(1, len(one_indices)):
            temp = (int) ((one_indices[i] - one_indices[i-1] - 2 ) / 2)
            result = result + temp
                        
        if flowerbed[-1] == 0:
            temp = (int) (len(flowerbed) - 1 - one_indices[-1]) / 2
            result = result + temp
                
        return result >= n
        
        
        
if __name__ == '__main__':
    c = CanPlaceFlowers()
    print(c.canPlaceFlowers([1,0,0,0,0,1], 2))
    print(c.canPlaceFlowers([1,0,0,0,1], 1))
    print(c.canPlaceFlowers([1,0,0,0,1], 2))
    print(c.canPlaceFlowers([1,0,0,0,1,0,0], 2))
