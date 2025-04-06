def gcd(a: int, b: int):
    small = b if a > b else a
    large = a ^ b ^ small

    r = 1
    while r > 0:
        q, r = divmod(large, small)
        large = small
        small = r

    return large


print(gcd(998244359987710471, 99824435698771045))  # =  1000000007
