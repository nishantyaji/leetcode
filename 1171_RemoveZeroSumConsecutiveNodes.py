#Problem 1171
#Solution is not my own. Peeked into the solution.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    
class RemoveZeroSumConsecutiveNodes:
        
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next == None:
            return head
        
        sum = 0       
        pre_head = ListNode(sum, head)
        present = head
        dict_sum = {sum: pre_head}
        while present is not None and present.val is not None:
            sum = sum + present.val
            dict_sum[sum] = present
            present = present.next
        
        present = pre_head
        sum = 0
        while present is not None and present.val is not None:
            sum = sum + present.val
            latest_node_on_sum = dict_sum[sum]
            present.next = latest_node_on_sum.next
            present = present.next
        
        return pre_head.next
    
    
    def formLinkedList(self, input: list) -> Optional[ListNode]:
        
        prev = None
        present = None 
        input.reverse()
        for i in input:
            present = ListNode(i, prev)
            prev = present
            
        return present 
    
    def printListNode(self, input: ListNode):
        
        while(input is not None):
            print(input.val)
            input = input.next
        
if __name__ == '__main__':
    r = RemoveZeroSumConsecutiveNodes()
    print(r.printListNode(r.removeZeroSumSublists(r.formLinkedList([1,3,2,-3,-2,5,5,-5,1]))))
    print(r.printListNode(r.removeZeroSumSublists(r.formLinkedList([1,-1, 3, 2, -2]))))
    print(r.printListNode(r.removeZeroSumSublists(r.formLinkedList([1,-1]))))
    print(r.printListNode(r.removeZeroSumSublists(r.formLinkedList([1,2,-3,3,1]))))
    print(r.printListNode(r.removeZeroSumSublists(r.formLinkedList([1,2,3,-3,4]))))
    print(r.printListNode(r.removeZeroSumSublists(r.formLinkedList([1,2,3,-3,-2]))))