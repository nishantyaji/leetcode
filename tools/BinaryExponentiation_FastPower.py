# base = 1000000007

def fast_pow(val: int, t: int, mod_base: int):
    if t > mod_base:
        return fast_pow(val, t % mod_base, base)

    res = 1
    mult = val
    while t > 0:
        if t & 1 == 1:
            res = (mult * res) % mod_base
        mult = (mult * mult) % mod_base
        t = t >> 1
    return res


a = 13
b = 17
base = 1000000007
print(fast_pow(a, b, base))
print(fast_pow(b, a, base))
print(pow(a, b, base))
print(pow(b, a, base))
