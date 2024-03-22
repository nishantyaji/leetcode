#Problem 234

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class PalindromeLinkedList:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return head
        running = head
        mylist = []
        while running is not None:
            mylist.append(running.val)
            running = running.next

        running = head
        i = len(mylist)-1
        limit = (int) (i+1)/2
        while i >= limit:
            if running.val != mylist[i]:
                return False
            running = running.next
            i -= 1

        return True
        