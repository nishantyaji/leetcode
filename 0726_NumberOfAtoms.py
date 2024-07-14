# Problem 726
import collections
import copy


class NumberOfAtoms:
    def countOfAtoms(self, formula: str) -> str:
        queue = self.get_q(formula)
        stack, mydict, val = [], collections.defaultdict(int), 1
        for q in queue:
            if q == ")":
                popped = False
                while stack and stack[-1] != "(":
                    popped = True
                    top = stack.pop()
                    if type(top) == type(1):
                        val = top
                    elif type(top) == type(collections.defaultdict(int)):
                        top_mul = self.multiply(top, val)
                        mydict = self.merge(mydict, top_mul)
                        val = 1
                    else:
                        mydict[top] += val
                        val = 1
                stack.pop()
                if popped:
                    stack.append(mydict)
                    mydict = collections.defaultdict(int)
            else:
                if q == "(":
                    val = 1
                stack.append(q)

        val = 1
        while stack:
            top = stack.pop()
            if type(top) == type(1):
                val = top
            elif type(top) == type(collections.defaultdict()):
                top_mul = self.multiply(top, val)
                mydict = self.merge(mydict, top_mul)
                # mydict = self.multiply(top, val)
                val = 1
            else:
                mydict[top] += val
                val = 1

        keys = list(mydict.keys())
        keys.sort()
        result = ""
        for key in keys:
            result += (key + ("" if mydict[key] == 1 else str(mydict[key])))

        return result

    def multiply(self, d: dict, m: int):
        d2 = copy.deepcopy(d)
        for k, v in d.items():
            d2[k] = m * v
        return d2

    def merge(self, d1: dict, d2: dict):
        d1_copy = copy.deepcopy(d1)
        for k, v in d2.items():
            if k not in d1_copy:
                d1_copy[k] = 0
            d1_copy[k] = d1_copy[k] + v
        return d1_copy

    def get_q(self, formula: str):
        upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        lower = "abcdefghijklmnopqrstuvwxyz"
        number = "1234567890"
        q = []
        temp, val = "", 0
        prev_up, prev_low, prev_num = False, False, False
        for i in range(len(formula)):
            if formula[i] in lower:
                temp += formula[i]
                prev_up, prev_low, prev_num = True, False, False
                val = 0
                continue
            elif formula[i] in upper:
                if prev_low or prev_up or prev_num:
                    if prev_num:
                        if val > 0:
                            q.append(val)
                    else:
                        if len(temp) > 0:
                            q.append(temp)
                    temp, val = "", 0
                temp += formula[i]
                prev_up, prev_low, prev_num = True, False, False
                val = 0
                continue
            elif formula[i] in number:
                val = 10 * val + int(formula[i])
                if prev_low or prev_up:
                    if len(temp) > 0:
                        q.append(temp)
                    temp = ""
                prev_up, prev_low, prev_num = False, False, True
                continue
            elif formula[i] in "()":
                if len(temp) > 0:
                    q.append(temp)
                elif val > 0:
                    q.append(val)
                temp, val = "", 0
                q.append(formula[i])
                continue
        if len(temp) > 0:
            q.append(temp)
        elif val > 0:
            q.append(val)
        return q


if __name__ == '__main__':
    n = NumberOfAtoms()
    print(n.countOfAtoms("((N42)24(OB40Li30CHe3O48LiNN26)33(C12Li48N30H13HBe31)21(BHN30Li26BCBe47N40)15(H5)16)14"))
    # "B18900Be18984C4200H5446He1386Li33894N50106O22638"
    print(n.countOfAtoms("H11He49NO35B7N46Li20"))
    # "B7H11He49Li20N47O35"
    print(n.countOfAtoms("H2O"))
    # H2O
    print(n.countOfAtoms("Mg(OH)2"))
    # H2MgO2
    print(n.countOfAtoms("K4(ON(SO3)2)2"))
    # K4N2O14S4
