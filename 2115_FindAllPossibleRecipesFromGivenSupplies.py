# Problem 2115
import collections
from typing import List


class FindAllPossibleRecipesFromGivenSupplies:

    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        # Using kahn's algo
        in_deg = {r: len(ingredients[i]) for i, r in enumerate(recipes)}
        mp = collections.defaultdict(set)
        for i in range(len(ingredients)):
            for x in ingredients[i]:
                mp[x].add(recipes[i])

        while True:
            temp = set()
            for s in supplies:
                for m in mp[s]:
                    in_deg[m] -= 1
                    if in_deg[m] == 0:
                        temp.add(m)
            if not temp:
                break
            supplies = temp

        return [r for r, val in in_deg.items() if val == 0]

    def findAllRecipes2(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:

        supplies = set(supplies)
        d = {r: set(ingredients[i]) for i, r in enumerate(recipes)}
        while True and d:
            keys = d.keys()
            changed = False
            remo = set()
            for k in keys:
                vals = d[k] - supplies
                if not vals:
                    supplies.add(k)
                    remo.add(k)
                    changed = True

            for k in remo:
                del d[k]

            if not changed:
                break
        return list(set(recipes).intersection(supplies))


if __name__ == '__main__':
    f = FindAllPossibleRecipesFromGivenSupplies()
    print(f.findAllRecipes(["bread"], [["yeast", "flour"]], ["yeast", "flour", "corn"]))
    print(f.findAllRecipes(["bread", "sandwich"], [["yeast", "flour"], ["bread", "meat"]], ["yeast", "flour", "meat"]))
    print(f.findAllRecipes(["bread", "sandwich", "burger"],
                           [["yeast", "flour"], ["bread", "meat"], ["sandwich", "meat", "bread"]],
                           ["yeast", "flour", "meat"]))
