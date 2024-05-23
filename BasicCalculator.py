# Problem 224


class BasicCalculator:
    def calculate(self, s: str) -> int:
        # Many things can be optimized here
        was_num = False
        stack = []
        num = 0
        for i, ch in enumerate(s):
            if ch in "0123456789":
                num = 10 * num + int(ch)
                was_num = True
            else:
                if was_num:
                    stack.append(num)
                if ch in "(+-":
                    stack.append(ch)
                if ch == ")":
                    token = ""
                    while stack[-1] != "(":
                        token = str(stack.pop()) + token
                    stack.pop()
                    ans = self.calc_token(token)
                    stack.append(ans)
                was_num, num = False, 0
        if was_num:
            stack.append(num)

        if stack:
            return self.calc_token("".join(list(map(lambda x: str(x), stack))))

        return ans

    def calc_token(self, s: str):
        s = s.replace("--", "+")
        ans, num = 0, 0
        sign = -1 if s[0] == '-' else 1
        if s[0] in "+-":
            s = s[1:]
        was_num = False
        for i, ch in enumerate(s):
            if ch in "0123456789":
                num = 10 * num + sign * int(ch)
                was_num = True
            elif ch in "+-":
                if was_num:
                    sign = 1
                    ans = ans + sign * num
                sign = 1 if ch == "+" else - 1
                was_num, num = False, 0

        if was_num:
            sign = 1
            ans = ans + sign * num

        return ans


if __name__ == '__main__':
    b = BasicCalculator()
    print(b.calculate("-(2+1)"))
    print(b.calculate("-2+1"))
    print(b.calculate("-2+ 1"))
    print(b.calculate("1-(     -2)"))
    print(b.calculate("1 + 1"))
    print(b.calculate(" 2-1 + 2 "))
    print(b.calculate("(1+(4+5+2)-3)+(6+8)"))
