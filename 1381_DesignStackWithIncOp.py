# Problem 1381

class CustomStack:

    def __init__(self, maxSize: int):
        self.q = []
        self.size = maxSize

    def push(self, x: int) -> None:
        if self.size > len(self.q):
            self.q.append(x)

    def pop(self) -> int:
        if self.q:
            return self.q.pop()
        else:
            return -1

    def increment(self, k: int, val: int) -> None:
        for i in range(min(k, len(self.q))):
            self.q[i] += val

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)