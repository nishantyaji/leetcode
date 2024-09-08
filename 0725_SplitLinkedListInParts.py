# Problem 725
from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def get_from_array(arr: list[int]):
        orig = l = ListNode()
        for i, a in enumerate(arr):
            l.val = a
            if i != len(arr) - 1:
                l.next = ListNode()
            l = l.next
        return orig


class SplitLinkedListInParts:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        lllen = 0
        pres = head
        while pres is not None:
            lllen += 1
            pres = pres.next

        q, r = divmod(lllen, k)

        result = []
        pres = head
        for outer in range(k):
            run_q = 0
            pres_orig = prev = pres
            while pres is not None and run_q < q:
                prev = pres
                pres = pres.next
                run_q += 1
            if pres is not None and r > 0:
                prev = pres
                pres = pres.next
                r -= 1
            if prev is not None:
                prev.next = None
                result.append(pres_orig)
            else:
                result.append(None)
        return result


if __name__ == '__main__':
    s = SplitLinkedListInParts()
    s.splitListToParts(ListNode.get_from_array([1, 2, 3]), 5)
    s.splitListToParts(ListNode.get_from_array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 3)
