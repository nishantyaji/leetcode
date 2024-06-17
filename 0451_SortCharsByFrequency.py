#problem 451

class SortCharsByFrequency:
    def frequencySort(self, s: str) -> str:
        mymap = {}
        max = 0
        if len(s) > 0:
            max = 1
        for i in s:
            if i in mymap:
                count = mymap[i]
                mymap[i] = count + 1
                if count + 1 > max:
                    max = count + 1
            else:
                mymap[i] = 1
        
        mylist = [None] * max
        
        for key, value in mymap.items():
            if mylist[value - 1] is None:
                mylist[value - 1] = []
            mylist[value - 1].append(key)
            
        returnstr = ""
        for i in range(0, max, 1):
            index = max - 1 - i
            if mylist[index] is not None:
                for j in mylist[index]:
                    returnstr += j * (index+1)
    
        return returnstr
    
if __name__ == '__main__':
    s = SortCharsByFrequency()
    print(s.frequencySort("tree"))
    print(s.frequencySort("cccaaa"))
    print(s.frequencySort("Aabb"))
    print(s.frequencySort("dabc"))