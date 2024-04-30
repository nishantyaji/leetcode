# Problem 258


class AddDigits:
    def addDigits(self, num: int) -> int:
        result = num
        while result > 9:
            num = result
            result = 0
            while num > 9:
                result += num % 10
                num = int(num / 10)
            result += num

        return result


if __name__ == '__main__':
    a = AddDigits()
    print(a.addDigits(100))
    print(a.addDigits(38))
