# Problem 2037
from typing import List


class MinNumOfMovesToSeatEveryone:
    # This method is O(nlogn) complexity
    # There is a method of O(m+n) complexity using counting sort
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        my_set, students_set = set(), set()
        my_set.update(list(filter(lambda x: x in students_set, seats)))
        for r in my_set:
            seats.remove(r)
            students.remove(r)
        seats.sort()
        students.sort()
        return sum(map(lambda x, y: abs(x - y), students, seats))
