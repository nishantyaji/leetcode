# Problem 2816
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class DoubleNumRepresentedAsLinkedList:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head

        carry = self.recurse(head)
        if carry > 0:
            temp = head
            head = ListNode(carry)
            head.next = temp

        return head

    def recurse(self, node):
        carry = 0
        if node.next is not None:
            carry = self.recurse(node.next)

        ans = node.val * 2 + carry
        node.val = ans % 10
        return int(ans / 10)
