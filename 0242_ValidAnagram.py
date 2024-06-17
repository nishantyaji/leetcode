# Problem 242

class ValidAnagram:
    def isAnagram(self, s: str, t: str) -> bool:
        letterCount = []
        for i in range(0, 26):
            letterCount.append(0)
        
        s = s.lower()
        t = t.lower()
        for ch in s:
            ordinal = ord(ch) - ord('a')
            letterCount[ordinal] = letterCount[ordinal] + 1
            
        for ch in t:
            ordinal = ord(ch) - ord('a')
            letterCount[ordinal] = letterCount[ordinal] - 1

        for i in range(0, 26):
            if letterCount[i] != 0:
                return False
            
        return True
                
if __name__ == '__main__':
    v = ValidAnagram()
    print(v.isAnagram("anagram", "nagaram"))
    print(v.isAnagram("rat", "car"))

    