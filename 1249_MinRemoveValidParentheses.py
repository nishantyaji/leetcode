# Problem 1249


class MinRemoveValidParentheses:
    def minRemoveToMakeValid(self, s: str) -> str:
        count = 0
        numnegative = 0
        for ch in s:
            if ch == "(":
                count += 1
            elif ch == ")":
                count -= 1
                if count < 0:
                    numnegative += 1
                    count = 0

        running = 0
        lastopenindices = []
        newstr = ""
        idx = -1
        for ch in s:
            if ch == "(":
                idx += 1
                running += 1
                newstr += ch
                if count > 0:
                    lastopenindices.append(idx)
                    if count + 1 == len(lastopenindices):
                        del lastopenindices[0]
            elif ch == ")":
                running -= 1
                if running >= 0:
                    idx += 1
                    newstr += ch
                else:
                    running = 0
            else:
                idx += 1
                newstr += ch

        if count > 0:
            for i in range(len(lastopenindices) - 1, -1, -1):
                newstr = newstr[:lastopenindices[i]] + newstr[lastopenindices[i] + 1:]

        return newstr


if __name__ == '__main__':
    m = MinRemoveValidParentheses()
    print(m.minRemoveToMakeValid("())()((("))
    print(m.minRemoveToMakeValid("))(("))
    print(m.minRemoveToMakeValid("lee(t(c)o)de)"))
    print(m.minRemoveToMakeValid("a)b(c)d"))
