# Problem 988

from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class SmallestStringStartingFromLeaf:
    minString = [26]
    
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        running_str = ""

        if root is not None:
            running_list = []
            self.recurse(root, running_list)
            for i in range(len(self.minString) - 1, -1, -1):
                running_str = running_str + str(chr(self.minString[i] + ord('a')))
                
        return running_str
        
    def compare(self, list1: List[int], list2: List[int]) -> int:
        # list1 - list2
        # if list1 appears earlier in lexicographic order then return negative
        print(list1)
        print(list2)
        if len(list1) != len(list2):
            small = list2 if len(list1) > len(list2) else list1
            considered_len = len(small)
            compare_result = self.compare(list1[:considered_len], list2[:considered_len])
            if compare_result == 0:
                return -1 if len(list1) < len(list2) else 1
            else:
                return compare_result
        else:
            for i in range(0, len(list1)):
                if list1[i] != list2[i]:
                    return list1[i] - list2[i]
            return 0
                            
             
    def recurse(self, present: TreeNode, incoming_running_list: List[int]):
        running_list = incoming_running_list.copy() 
        running_list.append(present.val)
        if present.left is None and present.right is None:
            compare_res = self.compare(running_list[::-1], self.minString[::-1])
            if compare_res < 0:
                self.minString = running_list
        else:
            if present.left is not None:
                self.recurse(present.left, running_list)
            if present.right is not None:
                self.recurse(present.right, running_list)
            
if __name__ == "__main__":
    s = SmallestStringStartingFromLeaf()