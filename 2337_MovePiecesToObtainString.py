# Problem 2337
import collections

"""
        observations:
        (le = lesser than or equal, ge = greater than or equal)
        1) any block with left as L and right R remains unchanged
        2) any block with left as R and right L will be le present value
        3) first block, if right is L will be le present value
        4) first block, if right is R will be ge present value
        5) last block, if left is L will be ge present value
        6) last block, if left is R will be le present value

        But the following observations will be used to code:
        1) for any L, the suffix sum will not decrease 
        2) for any R, the prefix sum will not decrease
        3) if you remove the underscores the start string should 
        be equal to the target string
"""


class MovePiecesToObtainString:
    def canChange(self, start: str, target: str) -> bool:
        if collections.Counter(start) != collections.Counter(target):
            return False
        und_dict, opp_dict, total, total_dict, opp = {"L": [], "R": []}, {"L": [], "R": []}, 0, {"L": 0, "R": 0}, {
            "L": "R", "R": "L"}

        for i, c in enumerate(start):
            if c == "_":
                total += 1
                continue
            und_dict[c].append(total)
            opp_dict[c].append(total_dict[opp[c]])
            total_dict[c] += 1

        idx_dict, total, total_dict = {"L": 0, "R": 0}, 0, {"L": 0, "R": 0}
        for i, c in enumerate(target):
            if c == "_":
                total += 1
                continue
            if (c == "L" and total > und_dict[c][idx_dict[c]]) or (c == "R" and total < und_dict[c][idx_dict[c]]) or \
                    total_dict[opp[c]] != opp_dict[c][idx_dict[c]]:
                return False
            total_dict[c] += 1
            idx_dict[c] += 1
        return True


if __name__ == '__main__':
    m = MovePiecesToObtainString()
    print(m.canChange("_L__R__RL", "L_____RLR"))
    print(m.canChange("_L__R__R_", "L______RR"))
    print(m.canChange("R_L_", "__LR"))
    print(m.canChange("_R", "R_"))
