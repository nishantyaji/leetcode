# Problem 1352

class ProductOfNumbers:

    def __init__(self):
        self.nums = []
        self.prod1 = []
        self.prod2 = []
        self.last_zero_idx = None

    def add(self, num: int) -> None:
        self.nums.append(num)
        if num == 0:
            self.prod1.append(0)
            self.prod2.append(1)
            self.last_zero_idx = len(self.prod1) - 1
        else:
            self.prod1.append(num if not self.prod1 else self.prod1[-1] * num)
            self.prod2.append(num if not self.prod2 else self.prod2[-1] * num)

    def getProduct(self, k: int) -> int:
        if self.last_zero_idx and self.last_zero_idx > len(self.nums) - k - 1:
            return 0
        else:
            if k >= len(self.nums):
                return self.prod2[-1] if self.last_zero_idx is None else 0
            return self.prod2[-1] // self.prod2[-k - 1]


if __name__ == '__main__':
    obj = ProductOfNumbers()
    obj.add(3)
    obj.add(0)
    obj.add(2)
    obj.add(5)
    obj.add(4)
    print(obj.getProduct(2))
    print(obj.getProduct(3))
    print(obj.getProduct(4))
    obj.add(8)
    print(obj.getProduct(2))
    #
    print()
    obj = ProductOfNumbers()
    obj.add(0)
    obj.add(5)
    obj.add(6)
    print(obj.getProduct(2))
    print(obj.getProduct(2))
    obj.add(8)
    print(obj.getProduct(4))
    obj.add(2)
