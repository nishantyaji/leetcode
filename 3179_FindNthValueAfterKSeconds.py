import copy


class FindNthValueAfterKSeconds:

    def valueAfterKSeconds(self, n: int, k: int) -> int:
        nums, base = [1] * n, 1000000007
        for i in range(k):
            for j in range(1, n):
                nums[j] = (nums[j - 1] + nums[j]) % base
        return nums[-1]


if __name__ == '__main__':
    w = FindNthValueAfterKSeconds()
    print(w.valueAfterKSeconds(5, 1000))
    print(w.valueAfterKSeconds(4, 5))
    print(w.valueAfterKSeconds(5, 3))
