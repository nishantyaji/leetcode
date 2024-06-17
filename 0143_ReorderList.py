# Problem 143
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class ReorderList:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None or head.next.next is None:
            return
        
        mylist = []
        present = head
        while present is not None:
            mylist.append(present)
            present = present.next

        for node in mylist:
            node.next = None
            
        forward = 0
        backward = 0

        while forward < len(mylist) + backward - 1:
            if backward < 0:
                mylist[backward].next = mylist[forward]
            backward -=1
            mylist[forward].next = mylist[backward]
            forward += 1
        
        if len(mylist) % 2 == 1:
            mylist[backward].next = mylist[forward]
        
        
if __name__ == '__main__':
    r = ReorderList()