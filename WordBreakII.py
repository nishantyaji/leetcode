# Problem 140

from typing import List


class WordBreakII:
    def __init__(self):
        self.s = ""
        self.words = []
        self.result = []

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        self.s, self.words = s, wordDict
        self.recurse(0, list())
        return self.result

    def recurse(self, index: int, running: List[str]):
        if index == len(self.s):
            self.result.append(" ".join(running))
            return
        if index > len(self.s):
            return

        for word in self.words:
            if self.s[index:].startswith(word):
                self.recurse(index + len(word), running + [word])


if __name__ == '__main__':
    w = WordBreakII()
    print(w.wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"]))
    w = WordBreakII()
    print(w.wordBreak("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"]))
    w = WordBreakII()
    print(w.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))
    # print(w.wordBreak(,))
