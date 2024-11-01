# Problem 1957
import functools


class DeleteCharsToMakeFancyString:
    def makeFancyString(self, s: str) -> str:
        # Code I wrote in June 2022
        cumNum = 1
        prevChar = "-"
        result = ""
        for ch in s:
            if ch == prevChar:
                cumNum = cumNum + 1
                if cumNum > 2:
                    continue
            else: 
                cumNum = 1
                prevChar = ch
            result = result + ch
        return result

    def makeFancyString2(self, s: str) -> str:
        # Code I wrote in Oct 2024
        def fn(a, b):
            if len(a) >= 2 and a[-1] == a[-2] and a[-1] == b:
                return a
            else:
                return a + b
        # This solution can be compressed to one
        # it is a tradeoff between brevity and clarity
        return functools.reduce(fn, s, "")

    def makeFancyString3(self, s: str) -> str:
        # Code I wrote in Oct 2024
        # One liner ugly little thing
        return "".join(list(map(lambda x: x[1], list(filter(lambda t: not (t[0] >= 2 and t[1] == s[t[0] - 1] and t[1] == s[t[0] - 2]), enumerate(s))))))


if __name__ == '__main__':
    d = DeleteCharsToMakeFancyString()
    print(d.makeFancyString("leeetcode"))
    print(d.makeFancyString("aaabaaaa"))
    print(d.makeFancyString("aab"))
