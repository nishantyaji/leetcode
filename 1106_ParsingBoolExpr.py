# Problem 1106
import functools


class ParsingBoolExpr:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = []
        ops = set(list("&!|"))
        for c in expression:
            if c == ")":
                args = []
                while stack and stack[-1] != "(":
                    args.append(stack.pop())
                stack.pop()
                o = stack.pop()
                val = self.do_op(o, args)
                stack.append(val)
                if len(stack) == 1:
                    return val
            else:
                val = ""
                if c == "t":
                    val = True
                elif c == "f":
                    val = False
                elif c in ops or c == "(":
                    val = c
                elif c == ",":
                    continue

                stack.append(val)
                pass

    def do_op(self, o: str, args: list[bool]):
        if o == "!":
            return not args[0]
        if o == "&":
            return functools.reduce(lambda x, y: x & y, args, True)
        if o == "|":
            return functools.reduce(lambda x, y: x | y, args, False)


if __name__ == '__main__':
    p = ParsingBoolExpr()
    print(p.parseBoolExpr("&(|(f))"))
    print(p.parseBoolExpr("|(f,f,f,t)"))
    print(p.parseBoolExpr("!(&(f,t))"))
