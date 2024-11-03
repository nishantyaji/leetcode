from typing import List


def insert_profit(self, num: int, my_list: List[int]):
    if len(my_list) == 0:
        my_list.append(num)
        return
    if len(my_list) == 1:
        if num < my_list[0]:
            my_list.insert(0, num)
        else:
            my_list.append(num)
        return

    start, end = 0, len(my_list) - 1
    while start <= end:
        mid = (start + end) // 2
        if my_list[mid] == num:
            start = mid
            break
        elif my_list[mid] > num:
            end = mid - 1
        else:
            start = mid + 1
    my_list.insert(start, num)
    return my_list