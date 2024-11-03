# https://leetcode.com/problems/find-the-winner-of-the-circular-game/editorial/

class JosephusProblem:

    def josephus(self, n: int, k: int) -> int:
        # This is O(n^2)
        start, arr = 0, list(range(1, n + 1))
        while len(arr) > 1:
            start = (start + k - 1) % len(arr)
            arr.pop(start)
        return arr[0]


'''
Initialize variables i and ans with 1 and 0 respectively.
Run a while loop till i <= N:
Update ans with (ans + k) % i.
Increment i by 1.
Return ans + 1 as the required answer.
'''


# GFG
# python code to implement Josephus problem

# Josephus function which will take
# two parameter N and K, number of people and positions respectively
# return the position of person survives
def Josephus(n, k):
    # initialize two variables i and ans
    i = 1
    ans = 0
    while (i <= n):
        # update the value of ans
        ans = (ans + k) % i
        i += 1

    # returning the required answer
    return ans + 1


# driver code
# let
n = 14
k = 2

result = Josephus(n, k)
print(result)

# This code is contributed by sarveshc111.
