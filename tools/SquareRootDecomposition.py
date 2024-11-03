import functools
import math
import operator


class SquareRootDecompositionExample:

    def solve(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        op = operator.add

        sd = SDHelper(nums, 0, op)
        print(sd.result)  # 45
        sd.update(4, 0)
        print(sd.query_inclusive(3, 5))  # 10
        print(sd.result)  # 40


class SDHelper:

    def __init__(self, nums: list[int], init_val: int, op):
        self.nums = nums
        self.sqrt = int(math.sqrt(len(nums)))
        self.content = []
        self.parent = []
        self.init_val = init_val
        self.op = op
        for i in range(self.sqrt):
            temp = self.nums[i * self.sqrt: min((i + 1) * self.sqrt, len(nums))]
            self.content.append(temp)
            self.parent.append(functools.reduce(self.op, temp, self.init_val))
        self.result = functools.reduce(self.op, self.parent, self.init_val)

    def update(self, pos_0_indexed: int, val: int):
        p_idx, idx = divmod(pos_0_indexed, self.sqrt)
        self.content[p_idx][idx] = val
        # the below statement can be sped up using an inverse operator
        # if the operation is associative and commutative
        self.parent[p_idx] = functools.reduce(self.op, self.content[p_idx], self.init_val)
        self.result = functools.reduce(self.op, self.parent, self.init_val)

    def query_inclusive(self, left: int, right: int):
        l_pidx, l_idx = divmod(left, self.sqrt)
        r_pidx, r_idx = divmod(right, self.sqrt)

        res = 0
        for p in range(l_pidx + 1, r_pidx):
            res += self.parent[p]
        if l_pidx != r_pidx:
            res += sum(self.content[l_pidx][l_idx:])
            res += sum(self.content[r_pidx][:r_idx + 1])
        else:
            res += sum(self.content[l_pidx][l_idx:r_idx + 1])
        return res


if __name__ == '__main__':
    s = SquareRootDecompositionExample()
    s.solve()
