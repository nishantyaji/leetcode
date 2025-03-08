# Problem 2379

class MinRecolorsToGetKConsecutiveBlackBlocks:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        arr = [1 if b == "B" else 0 for b in blocks]
        res = window = sum(arr[:k])
        for i in range(k, len(arr)):
            window = window - arr[i - k] + arr[i]
            res = max(res, window)
        return k - res
