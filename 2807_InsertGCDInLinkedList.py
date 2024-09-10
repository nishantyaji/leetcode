# Problem 2807
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class InsertGCDInLinkedList:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pres = head
        while pres is not None:
            if pres.next is not None:
                g = self.gcd(pres.val, pres.next.val)
                temp = ListNode(g, pres.next)
                pres.next = temp
                pres = pres.next
            pres = pres.next
        return head

    def gcd(self, a: int, b: int):
        small = b if a > b else a
        large = a ^ b ^ small

        r = 1
        while r > 0:
            q, r = divmod(large, small)
            large = small
            small = r

        return large
