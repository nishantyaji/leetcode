# Problem 3186

from typing import List


class MaxTotalDamageWithSpellCasting:
    def maximumTotalDamage(self, power: List[int]) -> int:
        if len(power) == 1:
            return power[0]

        power.sort()
        dist_dict, dist_power = dict(), []
        for p in power:
            if dist_power and dist_power[-1] == p:
                continue
            dist_power.append(p)
            dist_dict[p] = len(dist_dict)

        my_dict = {power[0]: power[0]}
        if (power[1] - 3 < power[0] < power[1]) or (power[1] < power[0] < power[1] + 3):
            my_dict[power[1]] = power[1]
        else:
            my_dict[power[1]] = my_dict[power[0]] + power[1]

        for p in power[2:]:
            this_res, this_max = p, -1
            if p in my_dict:
                this_res = ((my_dict[p]) + p)
            else:
                p_idx = dist_dict[p]
                for i in range(1, 6):
                    if p_idx - i >= 0 and dist_power[p_idx - i] < p - 2 and dist_power[p_idx - i] in my_dict:
                        this_max = max(this_max, my_dict[dist_power[p_idx - i]])
                if this_max > - 1:
                    this_res = this_max + p
            my_dict[p] = this_res

        return max(my_dict.values())


if __name__ == '__main__':
    w = MaxTotalDamageWithSpellCasting()
    print(w.maximumTotalDamage([5, 9, 2, 10, 2, 7, 10, 9, 3, 8]))
    print(w.maximumTotalDamage([2, 9, 10]))
    print(w.maximumTotalDamage([7, 1, 6, 6]))
    print(w.maximumTotalDamage([1, 1, 3, 4]))
    print(w.maximumTotalDamage([10]))
