# Problem 76


class MinWindowSubstring:

    @staticmethod
    def add_to_dict(my_dict, key) -> int:
        if key not in my_dict:
            my_dict[key] = 0
        my_dict[key] = my_dict[key] + 1
        return my_dict[key]

    @staticmethod
    def remove_from_dict(my_dict, key) -> int:
        if key in my_dict:
            my_dict[key] = my_dict[key] - 1
            if my_dict[key] == 0:
                del my_dict[key]

    @staticmethod
    def has_all(my_dict, ref_dict) -> bool:
        for key, ref_val in ref_dict.items():
            if key not in my_dict or my_dict[key] < ref_val:
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        result_ref = result = ["a"] * len(s)
        ref_dict = {}
        for ch in t:
            self.add_to_dict(ref_dict, ch)

        mydict = {}
        s = s + "1"
        left_ptr = 0
        right_ptr = 0

        while right_ptr < len(s):
            if not self.has_all(mydict, ref_dict):
                self.add_to_dict(mydict, s[right_ptr])
                right_ptr += 1
            else:
                while self.has_all(mydict, ref_dict):
                    self.remove_from_dict(mydict, s[left_ptr])
                    left_ptr += 1
                ans = s[left_ptr - 1: right_ptr]
                if len(ans) <= len(result):
                    result = ans

        return "" if result == result_ref else result


if __name__ == '__main__':
    m = MinimumWindowSubstring()
    print(m.minWindow("ADOBECODEBANC", "ABC"))
    print(m.minWindow("a", "a"))
    print(m.minWindow("a", "aa"))
