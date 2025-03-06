# Problem 2161
from typing import List


class PartitionArrayAccordingToGivenPivot:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        pref, suff, equ = [], [], []
        for n in nums:
            if n < pivot:
                pref.append(n)
            elif n > pivot:
                suff.append(n)
            else:
                equ.append(n)
        return pref + equ + suff
