# Problem 3298
from collections import Counter


class CountSubstrRearrangToContainStringII:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        l1, l2 = len(word1), len(word2)
        cntr, ref_cntr = Counter(), Counter(word2)
        cntr2_len = len(ref_cntr)

        """
        We use a 2-pointer (sliding window approach)
        But the constraint are very tight
        
        In every loop we might have to compare counters  (like in is_subset)
        But that might take as much as O(26*n) amortize
        
        Instead we maintain a key count
        the key count is incremented when we move right and add a character
        and when the incremented character reaches the same count as in word2
        
        We do the opposite when moving left.
        This reduces the complexity from O(26) to O(kn) where k ~1
        """

        left_limit = l1 - cntr2_len + 1
        key_count = 0
        res, prev_left, left, right = 0, 0, 0, 0
        while left <= left_limit:
            cntr[word1[right]] += 1
            if word1[right] in ref_cntr and cntr[word1[right]] == ref_cntr[word1[right]]:
                key_count += 1
            right += 1
            trimmed = False
            while key_count == cntr2_len:
                cntr[word1[left]] -= 1
                if word1[left] in ref_cntr and cntr[word1[left]] < ref_cntr[word1[left]]:
                    key_count -= 1
                left += 1
                trimmed = True
            if trimmed:
                # [left-1, right] is min required for condition
                res += (left - prev_left) * (l1 - right + 1)
                prev_left, prev_right = left, right
            if right == l1:
                break
        return res


"""

    def is_subset(self, superset: dict, subset: dict):
        for k, v in subset.items():
            if k not in superset or superset[k] < v:
                return False
        return True

"""
if __name__ == '__main__':
    c = CountSubstrRearrangToContainStringII()
    print(c.validSubstringCount("abcabc", "abc"))
    print(c.validSubstringCount("bcca", "abc"))
    print(c.validSubstringCount("abcabc", "aaabc"))
