import functools


class NonNegativeIntsWithoutConsecutive1s:
    def findIntegers(self, n: int) -> int:
        min_dict = {0: 1, 1: 2, 2: 3, 3: 3, 4: 4, 5: 5, 6: 5, 7: 5}
        if n < 8:
            return min_dict[n]

        bin_n = list(bin(n)[2:])
        num_digits = len(bin_n)
        result = self.recurse2power(num_digits - 1)

        if bin_n[1] == '1':
            result += self.recurse2power(len(bin_n[2:]))

        if len(bin_n) > 2 and bin_n[1] != '1':
            next_n = int("".join(bin_n[2:]), base=2)
            result += self.findIntegers(next_n)
        return result

        # for num_digits
        # We choose first digit as 1
        # 100011010
        # 1000 + findIntegers(11010)
        #
        # findIntegers(11010) =
        # If MSB = 0, r2p(4) i.e. num_digits - 1 = 4
        # If MSB = 1, then second integer is forced to be zero and then we get r2p(3)
        # We cannot choose MSB as 1 and the next most significant as 1
        #
        # Lets take example of 12
        # Assume first digit = 0
        # then result += r2p(num_digits(12) - 1) = r2p(3) = 5
        # Assume first digit = 1
        #   then second digit is 0,
        #   which reduces to length - 2 computation
        #   therefore take result += r2p(num_digits(12) - 2) = r2p(2) = 3
        #   We cannot second digit as 1 since the previous digit
        #         # has been chosen as 1 already
        #
        # Lets take example of 14 (1110)
        # Assume first digit = 0
        # then result += r2p(num_digits(12) - 1) = r2p(3) = 5
        # Assume first digit = 1
        #   then second digit is 0,
        #   which reduces to length - 2 computation
        #   therefore take result += r2p(num_digits(12) - 2) = r2p(2) = 3
        #   We cannot choose second digit as 1 since the previous digit
        # has been chosen as 1 already
        #
        #
        # findInteger(11...)
        # will always be r2p(numdigits-1) + r2p(numdigits-2)
        # for findInteger(101..) onwards say
        # we can do r2p(numdigits-1) + findInteger(bin_n[2:])



    @functools.cache
    def recurse2power(self, digits_from_end: int) -> int:
        if digits_from_end <= 0:
            return 0
        if digits_from_end == 1:
            # 0 , 1
            return 2
        if digits_from_end == 2:
            # 10, 01, 00
            return 3
        return self.recurse2power(digits_from_end - 2) + self.recurse2power(digits_from_end - 1)


if __name__ == '__main__':
    n = NonNegativeIntsWithoutConsecutive1s()
    print("12645112:  (Expect 121393)", n.findIntegers(12645112))
    # 121393   ..'0b110000001111001011111000'
    print("1: (Expect 2)", n.findIntegers(1))
    # 2
    print("2: (Expect 3)", n.findIntegers(2))
    # 3
    print("5: (Expect 5)", n.findIntegers(5))
    # 5
    print("6: (Expect 5)", n.findIntegers(6))
    # 5
    print("12: (Expect 8)", n.findIntegers(12))
    # 8
    print("13 (Expect 8):", n.findIntegers(13))
    # 8
    print("14 (Expect 8):", n.findIntegers(14))
    # 8
    print("15 (Expect 8):", n.findIntegers(15))
    # 8
    print("16: (Expect: 9)", n.findIntegers(16))
    # 9
    print("172: (Expect: 55)", n.findIntegers(172))
    # 55

