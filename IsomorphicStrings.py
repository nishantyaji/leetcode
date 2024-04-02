# Problem 205


class IsomorphicStrings:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        my_dict = {}
        rev_dict = {}
        for i in range(0, len(s)):
            if s[i] in my_dict and t[i] in rev_dict:
                if not (my_dict[s[i]] == t[i] and rev_dict[t[i]] == s[i]):
                    return False
            elif s[i] not in my_dict and t[i] not in rev_dict:
                my_dict[s[i]] = t[i]
                rev_dict[t[i]] = s[i]
            else:
                return False
        return True
