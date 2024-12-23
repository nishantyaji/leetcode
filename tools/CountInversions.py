import copy

def count_inversions(self, nums):
    # note to self : formulate a better algo
    nums_copy = copy.deepcopy(nums)
    nums_copy.sort()
    res = 0
    my_dict = {x: i for i, x in enumerate(nums)}
    for i in range(len(nums)):
        if nums_copy[i] != nums[i]:
            temp = nums[i]
            temp_pos = my_dict[nums_copy[i]]
            nums[temp_pos] = temp
            nums[i] = nums_copy[i]
            my_dict[nums[i]] = i
            my_dict[temp] = temp_pos
            res += 1

    return res



arr = [7, 6, 8, 5]