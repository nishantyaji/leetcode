# Problem 2429

class MinXOR:
    def minimizeXor(self, num1: int, num2: int) -> int:
        n1, n2, len1 = num1.bit_count(), num2.bit_count(), num1.bit_length()
        base, new_base = pow(2, len1-1), pow(2, len1)
        stack, i, ans = [], 0, 0
        while i < n2 and base >= 1:
            if base & num1 > 0:
                ans |= base
                i += 1
            else:
                stack.append(base)
            base >>= 1

        if i == n2:
            return ans

        while i < n2:
            if stack:
                base = stack.pop()
                ans |= base
            else:
                ans |= new_base
                new_base <<= 1
            i += 1
        return ans


if __name__ == '__main__':
    m = MinXOR()
    print(m.minimizeXor(3, 5))
    print(m.minimizeXor(1, 12))
