# Problem 2

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class AddTwoNumbers:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None or l2 is None:
            return None

        head = None
        carry = 0
        prev = None
        while l1 is not None and l2 is not None:
            ans = l1.val + l2.val + carry
            carry = int(ans / 10)
            node = ListNode(ans % 10)
            if not head:
                head = node
            else:
                prev.next = node
            prev = node
            l1 = l1.next
            l2 = l2.next

        for l in [l1, l2]:
            while l is not None:
                ans = l.val + carry
                carry = int(ans / 10)
                node = ListNode(ans % 10)
                prev.next = node
                prev = node
                l = l.next

        if carry > 0:
            prev.next = ListNode(carry)

        return head
