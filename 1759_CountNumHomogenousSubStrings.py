# Problem 1759

class CountNumHomogenousSubStrings:
    def countHomogenous(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        base = int(1e9 + 7)
        prev_char = s[0]
        running_count = 1
        result_sum = 0
        for ch in s[1:]:
            if ch == prev_char:
                running_count += 1
            else:
                result_sum = (result_sum + self.calculate(running_count, base)) % base
                running_count = 1
                prev_char = ch

        result_sum = (result_sum + self.calculate(running_count, base)) % base
        return result_sum

    def calculate(self, count: int, base: int) -> int:
        return int((count * (count + 1)) / 2 % base)


if __name__ == '__main__':
    c = CountNumHomogenousSubStrings()
    print(c.countHomogenous("abbcccaa"))
    print(c.countHomogenous("xy"))
    print(c.countHomogenous("zzzzz"))
