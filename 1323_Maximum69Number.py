# Problem 1323


class Maximum69Number:
    def maximum69Number(self, num: int) -> int:
        resultStr = ""
        found = False
        for character in str(num):
            if found == False and character == "6":
                first = "9"
                found = True
            else:
                first = character
            resultStr = resultStr + first
        return int(resultStr)


if __name__ == '__main__':
    m = Maximum69Number()
    print(m.maximum69Number(9669))
