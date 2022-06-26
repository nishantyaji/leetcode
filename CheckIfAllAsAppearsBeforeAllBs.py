# Problem 2124


class CheckIfAllAsAppearsBeforeAllBs:

    def checkString(self, s: str) -> bool:
        bool_first_index_b = False
        for ch in s:
            if ch == 'a':
                if bool_first_index_b == False:
                    continue
                else:
                    return False
            elif bool_first_index_b == False:
                bool_first_index_b = True

        return True


if __name__ == '__main__':
    c = CheckIfAllAsAppearsBeforeAllBs()
    print(c.checkString("aaabbb"))
    print(c.checkString("abab"))
