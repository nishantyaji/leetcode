import sys


def kadande_impl(x):
    cur_max_sum, max_sum = -sys.maxsize, -sys.maxsize
    for y in x:
        cur_max_sum = max(cur_max_sum + y, y)
        max_sum = max(max_sum, cur_max_sum)
    return max_sum


arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(kadande_impl(arr))
