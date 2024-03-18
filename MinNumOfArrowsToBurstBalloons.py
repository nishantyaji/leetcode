#Problem 452

from typing import List
from typing import Optional

class MinNumOfArrowsToBurstBalloons:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points, key=lambda x: 10000*x[0] + x[1])
        count = 0
        overlapwindow = None
        for i in range(0, len(points)-1):
            listConsidered = points[i] if overlapwindow == None else overlapwindow
            temp = self.overlap(listConsidered, points[i+1])
            if None == temp:
                count += 1
                overlapwindow = None
            else:
                overlapwindow = temp
        
        count += 1
        return count


    def overlap(self, list1: List, list2: List) -> Optional[List]:
        left = min(list1[1], list2[0])
        if left > list1[1] or left < list2[0]:
            return None
        right = min(list1[1], list2[1])
        return [left, right]

if __name__ == '__main__':
    m = MinNumOfArrowsToBurstBalloons()
    print(m.findMinArrowShots([[10,16],[2,8],[1,6],[7,12]]))
    print(m.findMinArrowShots([[1,2],[3,4],[5,6],[7,8]]))
    print(m.findMinArrowShots([[1,2],[2,3],[3,4],[4,5]]))