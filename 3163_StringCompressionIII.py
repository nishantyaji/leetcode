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


if __name__ == '__main__':
    w = StringCompressionIII()
    print(w.compressedString("abcde"))
    print(w.compressedString("aaaaaaaaaaaaaabb"))
    print(w.compressedString("aaabbbbcccccccccc"))
    print(w.compressedString("a"))
    print(w.compressedString("ab"))
