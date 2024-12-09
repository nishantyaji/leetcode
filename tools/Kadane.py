import sys


def kadane_impl(x):
    cur_max_sum, max_sum = -sys.maxsize, -sys.maxsize
    for y in x:
        cur_max_sum = max(cur_max_sum + y, y)
        max_sum = max(max_sum, cur_max_sum)
    return max_sum


def presentprefix_minus_minprefix(x):

    """
    The answer is the max among
    the prefix sum at index i and the min prefix sum that occurs before index i
    """

    min_prefix = 0
    prefix = 0
    max_sum = -sys.maxsize
    for a in x:
        prefix += a
        min_prefix = min(min_prefix, prefix)
        max_sum = max(max_sum, prefix - min_prefix)
    return max_sum

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(kadane_impl(arr))
