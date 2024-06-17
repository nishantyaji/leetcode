# Problem 3068


from typing import List


class FindMaxSumOfNodeValues:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:

        sum_nums = sum(nums)
        triples = []
        max_np, max_np_idx = -1000000001, -1
        for idx, num in enumerate(nums):
            diff = (num ^ k) - num
            if diff > 0:
                triples.append((diff, idx))
            else:
                if max_np < diff:
                    max_np = diff
                    max_np_idx = idx

        triples.sort(key=lambda x: x[0], reverse=True)
        if len(triples) % 2 == 1:
            if triples[-1][0] > abs(max_np):
                triples.append((max_np, max_np_idx))
            else:
                triples = triples[:-1]
        return sum_nums + sum([x[0] for x in triples])


if __name__ == '__main__':
    f = FindMaxSumOfNodeValues()
    print(f.maximumValueSum([67, 13, 79, 13, 75, 11, 0, 41, 94], 7,
                            [[0, 1], [3, 7], [4, 7], [6, 5], [6, 0], [0, 2], [7, 2], [7, 8]]))
    print(f.maximumValueSum([1, 2, 1], 3, [[0, 1], [0, 2]]))
    print(f.maximumValueSum([2, 3], 7, [[0, 1]]))
    print(f.maximumValueSum([7, 7, 7, 7, 7, 7], 3, [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5]]))
    # print(f.maximumValueSum())
