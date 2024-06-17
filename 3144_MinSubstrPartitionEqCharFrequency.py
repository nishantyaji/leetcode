# Problem 3144

class MinSubstrPartitionEqCharFrequency:

    def minimumSubstringsInPartition(self, s: str) -> int:
        dp = {-1: 0, 0: 1}

        for i in range(1, len(s)):
            my_dict = {s[i]: 1}
            min_val = dp[i - 1] + 1
            for j in range(i - 1, -1, -1):
                ch = s[j]
                if ch not in my_dict:
                    my_dict[ch] = 0
                my_dict[ch] = my_dict[ch] + 1
                if self.is_bal(my_dict):
                    min_val = min(min_val, 1 + dp[j - 1])

            dp[i] = min_val

        return dp[len(s) - 1]

    def is_bal(self, my_dict: dict) -> bool:
        vals = my_dict.values()
        return min(vals) == max(vals)


if __name__ == '__main__':
    m = MinSubstrPartitionEqCharFrequency()
    print(m.minimumSubstringsInPartition("abababaccddb"))
    print(m.minimumSubstringsInPartition("aab"))
    print(m.minimumSubstringsInPartition("xwjhpcyyyyrppppppppcccsqqqrrrssxxxfnnnhhjqnrsrnnnttt"))
    print(m.minimumSubstringsInPartition("fabccddg"))
