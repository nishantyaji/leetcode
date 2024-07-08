# Problem 1823
class FindWinnerOfCircularGame:
    def findTheWinner(self, n: int, k: int) -> int:
        start, arr = 0, list(range(1, n + 1))
        while len(arr) > 1:
            start = (start + k - 1) % len(arr)
            arr.pop(start)
        return arr[0]


if __name__ == '__main__':
    f = FindWinnerOfCircularGame()
    print(f.findTheWinner(5, 2))
    # 3
    print(f.findTheWinner(6, 5))
    # 1
