# Problem 1957


class DeleteCharsToMakeFancyString:
    def makeFancyString(self, s: str) -> str:
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


if __name__ == '__main__':
    d = DeleteCharsToMakeFancyString()
    print(d.makeFancyString("leeetcode"))
    print(d.makeFancyString("aaabaaaa"))
    print(d.makeFancyString("aab"))
