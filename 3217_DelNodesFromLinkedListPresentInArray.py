# Problem 3217
from typing import List, Optional


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

    def display(self):
        temp = self
        l = []
        while temp is not None:
            l.append(str(temp.val))
            temp = temp.next
        print(" ".join(l))


class DelNodesFromLinkedListPresentInArray:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        num_set = set(nums)
        orig = ListNode()
        pres = orig
        while head is not None:
            if head.val not in num_set:
                pres.next = ListNode(head.val)
                pres = pres.next
            head = head.next
        return orig.next


if __name__ == '__main__':
    d = DelNodesFromLinkedListPresentInArray()
    (d.modifiedList([9, 2, 5], ListNode.get_from_array([2, 10, 9]))).display()
    (d.modifiedList([1, 2, 3], ListNode.get_from_array([1, 2, 3, 4, 5]))).display()
    (d.modifiedList([1], ListNode.get_from_array([1, 2, 1, 2, 1, 2]))).display()
    (d.modifiedList([5], ListNode.get_from_array([1, 2, 3, 4]))).display()
