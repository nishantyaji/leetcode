# Problem 2487

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class RemoveNodesFromLinkedList:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        q = [head]
        while head is not None:
            this_val = head.val
            while len(q) > 0 and this_val > q[-1].val:
                q.pop()
            q.append(head)
            head = head.next

        prev = q[0]
        for node in q[1:]:
            prev.next = node
            prev = node
        prev.next = None
        return q[0]
