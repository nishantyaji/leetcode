# Problem 301
from typing import List


class RemoveInvalidParameters:
    def __init__(self):
        self.max_pos = 0
        self.result = []

    def removeInvalidParentheses(self, s: str) -> List[str]:
        self.recurse(s, 0, 0, [])
        self.result = list(set(self.result))
        return self.result

    def recurse(self, s: str, index: int, run_sum: int, running: List[str]):
        if run_sum < 0 or run_sum - (len(s) - index) > 0:
            return
        if index == len(s):
            this_str = "".join(running)
            this_stack = self.get_stack(this_str)
            if len(this_stack) > 0:
                return
            if len(running) > self.max_pos:
                self.max_pos = len(running)
                self.result = [this_str]
            elif len(running) == self.max_pos:
                self.result.append(this_str)
            return

        this_val = 0
        if s[index] == "(":
            this_val = 1
        elif s[index] == ")":
            this_val = -1

        if run_sum + this_val >= 0:
            self.recurse(s, index + 1, run_sum + this_val, running + [s[index]])
        self.recurse(s, index + 1, run_sum, running)

    def form_string(self, s, excluded: List[int]) -> str:
        return "".join([x for idx, x in enumerate(s) if idx not in excluded])

    def get_stack(self, s):
        stack = []
        for idx, ch in enumerate(s):
            if ch == "(":
                stack.append([idx, ch])
            elif ch == ")":
                if stack and stack[-1][1] == "(":
                    stack.pop()
                else:
                    stack.append([idx, ch])

        return stack


if __name__ == '__main__':
    r = RemoveInvalidParameters()
    print(r.removeInvalidParentheses("((((((((((((((((((((aaaaa"))

    r = RemoveInvalidParameters()
    print(r.removeInvalidParentheses("(a)())()"))

    r = RemoveInvalidParameters()
    print(r.removeInvalidParentheses("(()))()())(()"))

    r = RemoveInvalidParameters()
    print(r.removeInvalidParentheses("(r(()()("))
    # ["r()()","r(())","(r)()","(r())"]...

    r = RemoveInvalidParameters()
    print(r.removeInvalidParentheses("(("))

    r = RemoveInvalidParameters()
    print(r.removeInvalidParentheses("n"))

    r = RemoveInvalidParameters()
    print(r.removeInvalidParentheses("()())()"))

    r = RemoveInvalidParameters()
    print(r.removeInvalidParentheses(")("))
