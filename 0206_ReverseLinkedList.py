#Problem 206

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class ReverseLinkedList:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next == None:
            return head
        
        present = head
        prev = None
        while True:
            future = present.next 
            present.next = prev
            prev = present
            if future is not None:
                present = future
            else:
                break
        
        return prev
        
if __name__ == '__main__':
    r = ReverseLinkedList()