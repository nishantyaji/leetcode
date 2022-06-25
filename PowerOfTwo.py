# Problem 231


class PowerOfTwo:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        else:
            while n > 1:
                rem = n % 2
                if rem > 0:
                    return False
                n = n / 2
            return True


if __name__ == '__main__':
    p = PowerOfTwo()
    print(p.isPowerOfTwo(1024))
