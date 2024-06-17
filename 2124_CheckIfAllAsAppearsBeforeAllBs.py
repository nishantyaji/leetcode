# Problem 2124


class CheckIfAllAsAppearsBeforeAllBs:

    def checkString(self, s: str) -> bool:
        bool_first_index_b = False
        for ch in s:
            if ch == 'a':
                if not bool_first_index_b:
                    continue
                else:
                    return False
            elif not bool_first_index_b:
                bool_first_index_b = True

        return True


if __name__ == '__main__':
    c = CheckIfAllAsAppearsBeforeAllBs()
    print(c.checkString("aaabbb"))
    print(c.checkString("abab"))
