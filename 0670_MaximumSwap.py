# Problem 670


class MaximumSwap:
    def maximumSwap(self, num: int) -> int:
        num_str = str(num)
        max_temp, max_idx = "0", -1
        max_array = [-1] * len(num_str)
        for i in range(len(num_str) - 1, -1, -1):
            ch = num_str[i]
            if ch > max_temp:
                max_temp = ch
                max_idx = i
            max_array[i] = max_idx

        for i in range(0, len(num_str)):
            if i != max_array[i] and num_str[i] != num_str[max_array[i]]:
                return self.swap(num_str, i, max_array[i])
        return int(num_str)

    def swap(self, s: str, first: int, second: int):
        return int(s[0:first] + s[second] + s[first + 1:second] + s[first] + s[second + 1:])


if __name__ == '__main__':
    m = MaximumSwap()
    print(m.maximumSwap(1993))
    print(m.maximumSwap(98368))
