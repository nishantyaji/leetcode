# Problem 3163
class StringCompressionIII:
    def compressedString(self, word: str) -> str:
        count = 1
        prev = word[0]
        result = ""
        for ch in word[1:]:
            if ch == prev:
                count += 1
                if count == 9:
                    result += ("9" + ch)
                    count = 0
            else:
                if count > 0:
                    result += (str(count) + prev)
                count = 1
                prev = ch
        if count > 0:
            result += (str(count) + prev)
        return result

    def compressedString(self, word: str) -> str:
        res, prev, cnt = [], "~", 0

        def append_(cnt, prev):
            q, r = divmod(cnt, 9)
            temp = ["9" + prev] * q
            if r:
                temp += [str(r), prev]
            return temp

        for c in word:
            if prev != c and prev != "~":
                res += append_(cnt, prev)
                cnt = 0
            prev = c
            cnt += 1
        res += append_(cnt, prev)
        return "".join(res)

if __name__ == '__main__':
    w = StringCompressionIII()
    print(w.compressedString("abcde"))
    print(w.compressedString("aaaaaaaaaaaaaabb"))
    print(w.compressedString("aaabbbbcccccccccc"))
    print(w.compressedString("a"))
    print(w.compressedString("ab"))
