# Problem 17
from typing import List

class LetterCombinationsPhoneNumber:
    def letterCombinations(self, digits: str) -> List[str]:
        lettermap = {'2' : ["a", "b", "c"],
                     '3' : ["d", "e", "f"],
                     '4' : ["g", "h", "i"],
                     '5' : ["j", "k", "l"],
                     '6' : ["m", "n", "o"],
                     '7' : ["p", "q", "r", "s"],
                     '8' : ["t", "u", "v"],
                     '9' : ["w", "x", "y", "z"]}
        result = []
        self.recurse(lettermap, digits, 0, "", result)
        return result
        
    def recurse(self, lettermap, digits: str, idx: int, running: str, result: List):
        if idx == len(digits):
            result.append(running)
            return
        digit = digits[idx]
        for char in lettermap[digit]:
            newrunning = running + char
            self.recurse(lettermap, digits, idx+1, newrunning, result)
    
if __name__ == '__main__':
    l = LetterCombinationsPhoneNumber()
    print(l.letterCombinations("23"))
    print(l.letterCombinations(""))
    print(l.letterCombinations("2"))