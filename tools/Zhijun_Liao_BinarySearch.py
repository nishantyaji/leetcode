def binary_search(array) -> int:
    #https://leetcode.com/discuss/general-discussion/786126/python-powerful-ultimate-binary-search-template-solved-many-problems
    def condition(value) -> bool:
        pass

    search_space = []
    left, right = min(search_space), max(search_space) # could be [0, n], [1, n] etc. Depends on problem
    while left < right:
        mid = left + (right - left) // 2
        if condition(mid):
            right = mid
        else:
            left = mid + 1
    return left


# after exiting the while loop, left is the minimal k satisfying the condition function;


# suggest
# 1482_MinNumDaysToMakeMBouquets
# or 1552_MagneticForceBetweenTwoBalls
# for reliable implementation