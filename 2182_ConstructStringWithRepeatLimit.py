# Problem 2182
class ConstructStringWithRepeatLimit:

    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        cntr = {x: 0 for x in "abcdefghijklmnopqrstuvwxyz"}
        for c in s:
            cntr[c] += 1
        stack = []  # this will help us maintain lexicographic order
        for k, v in cntr.items():
            if v > 0:
                stack.append([k, v])

        res, count = [], 0
        for _ in range(len(s)):
            if count == repeatLimit:
                large = stack.pop()
                if stack:
                    res += [stack[-1][0]]
                    stack[-1][1] -= 1
                    if stack[-1][1] == 0:
                        stack.pop()
                    count = 0
                else:
                    break
                stack.append(large)
            else:
                res += [stack[-1][0]]
                stack[-1][1] -= 1
                if stack[-1][1] == 0:
                    stack.pop()
                    count = 0
                else:
                    count += 1
        return "".join(res)


def repeatLimitedStringSlow(self, s: str, repeatLimit: int) -> str:
    # this is slow since we iterate over the key of the dictionary
    # (which might be upto 26 in number)
    cntr = {x: 0 for x in "zyxwvutsrqponmlkjihgfedcba"}
    for c in s:
        cntr[c] += 1
    for c in "zyxwvutsrqponmlkjihgfedcba":
        if cntr[c] == 0:
            del cntr[c]

    res, count = [], 0
    for _ in range(len(s)):
        keys = list(cntr.keys())
        if count == repeatLimit:
            if len(keys) > 1:
                count = 0
                res += [keys[1]]
                cntr[keys[1]] -= 1
                if cntr[keys[1]] == 0:
                    del cntr[keys[1]]
            else:
                break
        else:
            res += [keys[0]]
            cntr[keys[0]] -= 1
            if cntr[keys[0]] == 0:
                del cntr[keys[0]]
                count = 0
            else:
                count += 1
    return "".join(res)


if __name__ == '__main__':
    c = ConstructStringWithRepeatLimit()
    print(c.repeatLimitedString("cczazcc", 3))  # "zzcccac"
    print(c.repeatLimitedString("aababab", 2))  # "bbabaa"
    print(c.repeatLimitedString("ccccccccc", 3))  # "ccc"
