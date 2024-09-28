# Problem 641

class MyCircularDeque:

    def __init__(self, k: int):
        self.q = []
        self.k = k
        self.sz = 0

    def insertFront(self, value: int) -> bool:
        if self.sz == self.k:
            return False
        self.q = [value] + self.q
        self.sz += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.sz == self.k:
            return False
        self.q += [value]
        self.sz += 1
        return True

    def deleteFront(self) -> bool:
        if self.sz == 0:
            return False
        self.sz -= 1
        self.q.pop(0)
        return True

    def deleteLast(self) -> bool:
        if self.sz == 0:
            return False
        self.sz -= 1
        self.q.pop()
        return True

    def getFront(self) -> int:
        if self.sz == 0:
            return -1
        return self.q[0]

    def getRear(self) -> int:
        if self.sz == 0:
            return -1
        return self.q[self.sz - 1]

    def isEmpty(self) -> bool:
        return self.sz == 0

    def isFull(self) -> bool:
        return self.sz == self.k

if __name__ == '__main__':
    obj = MyCircularDeque(3)
    print(obj.insertLast(1))
    print(obj.insertLast(2))
    print(obj.insertFront(3))
    print(obj.insertFront(4))
    print(obj.getRear())
    print(obj.isFull())
    print(obj.deleteLast())
    print(obj.insertFront(4))
    print(obj.getFront())
