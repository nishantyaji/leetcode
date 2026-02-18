# Problem 67

class AddBinary:
    def addBinary(self, a: str, b: str) -> str:
        return format(int(a, 2) + int(b, 2), "b")