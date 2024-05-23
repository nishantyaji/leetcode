# problem 282

from typing import List
import re

class ExpressionAddOperators:

    def __init__(self):
        self.num = ""
        self.target = 0
        self.result = []

    def addOperators(self, num: str, target: int) -> List[str]:
        self.num, self.target = num, target
        self.recurse(0, "", "")
        return self.result

    def recurse(self, index_on: int, running: str, prev_token: str):
        prev_token = prev_token + self.num[index_on]
        if len(prev_token) and str(int(prev_token)) != prev_token:
            return
        if index_on == len(self.num) - 1:
            running = running + self.num[index_on]
            if eval(running) == self.target:
                self.result.append(running)
            return

        self.recurse(index_on + 1, running + self.num[index_on], prev_token + self.num[index_on])
        for ch in ["+", "-", "*"]:
            self.recurse(index_on + 1, running + self.num[index_on] + ch, "")


if __name__ == '__main__':
    e = ExpressionAddOperators()
    print(e.addOperators("105", 5))
    # ["1*0+5","10-5"]...
    e = ExpressionAddOperators()
    print(e.addOperators("123", 6))
    e = ExpressionAddOperators()
    print(e.addOperators("232", 8))
    e = ExpressionAddOperators()
    print(e.addOperators("3456237490", 9191))
