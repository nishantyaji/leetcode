# Problem 344
from typing import List


class ReverseString:

    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(0,  1 + ((len(s)-1)//2)):
            temp = s[i]
            s[i] = s[len(s)-1-i]
            s[len(s)-1-i] = temp

