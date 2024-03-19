# Problem 621
from typing import List

class TaskScheduler:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        alphacount = [0] * 26
        baseord = ord('A')
        maxcount = 0
        
        for t in tasks: 
            idx = ord(t) - baseord
            alphacount[idx] = alphacount[idx] + 1
            if alphacount[idx] > maxcount:
                maxcount = alphacount[idx]
        
        num_alpha_max = 0        
        for count in alphacount:
            if count == maxcount:
                num_alpha_max += 1
        
        
        countone = (n+1) * (maxcount-1) + num_alpha_max
         
        return max(countone, len(tasks))
if __name__ == '__main__':
    t = TaskScheduler()
    print(t.leastInterval(["A","A","A","B","B","B"], 2))
    print(t.leastInterval(["A","C","A","B","D","B"], 1))
    print(t.leastInterval(["A","A","A", "B","B","B"], 3))