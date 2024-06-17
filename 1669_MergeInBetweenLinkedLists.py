#Problem 1669

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MergeInBetweenLinkedLists:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        
        list2present = list2
        while list2present.next != None:
            list2present = list2present.next
        list2end = list2present
        
        list1present = list1
        for i in range(0, b+1):
            list1next = list1present.next
            if i == a - 1:
                list1present.next = list2
            list1present = list1next
            
        list2end.next = list1next
        return list1
    
if __name__ == '__main__':
    m = MergeInBetweenLinkedLists()