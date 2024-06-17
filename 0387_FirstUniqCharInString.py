#Problem 387

class FirstUniqCharInString:
    def firstUniqChar(self, s: str) -> int:
        singleset = set()
        multiset = set()
        
        for i in s:
            if i in multiset:
                continue
            elif i in singleset:
                singleset.remove(i)
                multiset.add(i)
            else:
                singleset.add(i)
                
        for i in range(0, len(s)):
            if s[i] in singleset:
                return i
            
        return -1
        
        
if __name__ == '__main__':
    f = FirstUniqCharInString()
    print(f.firstUniqChar("leetcode"))
    print(f.firstUniqChar("loveleetcode"))
    print(f.firstUniqChar("aabb"))


    