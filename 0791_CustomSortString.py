# Problem 791

class CustomSortString:
    def customSortString(self, order: str, s: str) -> str:
        
        result = ""
        includedict = {}
        for ch in s:
            if ch in includedict:
                count = includedict[ch]
                includedict[ch] = count + 1
            else:
                includedict[ch] = 1

        for i in order:
            if i in includedict:
                result = result + i*includedict[i]
                del includedict[i]
                
        for ch, count in includedict.items():
            result = result + ch * count
        
        return result
            

    
if __name__ == '__main__':
    c = CustomSortString()
    print(c.customSortString("cba", "abcd"))
    print(c.customSortString("bcafg", "abcd"))