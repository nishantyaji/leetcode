"""
            def check(numm: int, index: int, holder: list[list[int]]):
                if holder[0][0] < 0:
                    holder[0] = [numm, index]
                elif holder[1][0] < 0:
                    if holder[0][0] < numm:
                        holder[0], holder[1] = [numm, index], holder[0]
                    else:
                        holder[1] = [numm, index]
                else:
                    if numm > holder[0][0]:
                        holder[0], holder[1] = [numm, index], holder[0]
                    elif holder[1][0] < numm < holder[0][0]:
                        holder[1] = [numm, index]

            res_holder = [[-1, -1], [-1, -1]]
            for i in range(len(a) - 1, idx, -2):
                if a[i] - a[i-1] > new_max_diff:
                    new_max_diff = a[i] - a[i-1]
                    new_max_diff_idx = i
                    check(new_max_diff, new_max_diff_idx, res_holder)
"""

