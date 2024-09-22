# Problem 214

class ShortestPalindrome:

    def shortestPalindrome(self, s: str) -> str:
        # This is O(n^2)
        # Better approaches are
        # Manacher's algo
        # Rolling Hash based algo
        # KMP algo
        pos = []
        lens = len(s)
        for i in range(int((lens - 1) / 2), -1, -1):
            eq = True
            for j in range(1, i + 1):
                if s[i - j] != s[i + j]:
                    eq = False
                    break
            if eq:
                pos.append(s[2 * i + 1:][::-1] + s)
                break

        for i in range(lens // 2 - 1, -1, -1):
            eq = True
            for j in range(0, min(i + 1, lens - i - 1)):
                if s[i - j] != s[i + j + 1]:
                    eq = False
                    break
            if eq:
                pos.append(s[2 * (i + 1):][::-1] + s)
                break

        pos.sort(key=len)
        return pos[0]


if __name__ == '__main__':
    s = ShortestPalindrome()
    print(s.shortestPalindrome("abb"))
    print(s.shortestPalindrome("abbacd"))
    print(s.shortestPalindrome("aacecaaa"))
    print(s.shortestPalindrome("abcd"))
