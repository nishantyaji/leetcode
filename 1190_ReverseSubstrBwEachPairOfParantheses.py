# Problem 1190


class ReverseSubstrBwEachPairOfParantheses:

    def reverseParentheses(self, s: str) -> str:
        stack = []
        for i, c in enumerate(s):
            if c == ")":
                temp = ""
                while stack and stack[-1] != "(":
                    # We need to reverse because we are within bracket
                    # Both single char and strings will be reversed.
                    # Essentially no-op for single char
                    temp += stack.pop()[::-1]
                stack.pop()
                stack.append(temp)
            else:
                stack.append(c)
        return "".join(stack)


if __name__ == '__main__':
    r = ReverseSubstrBwEachPairOfParantheses()
    print(r.reverseParentheses("a(bcdefghijkl(mno)p)q"))
    # "apmnolkjihgfedcbq"
    print(r.reverseParentheses("(abcd)"))
    # dcba
    print(r.reverseParentheses("(u(love)i)"))
    # iloveu
    print(r.reverseParentheses("(ed(et(oc))el)"))
    # leetcode
