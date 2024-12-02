# Problem 1455

class CheckIfWordOccursAsPrefixOfAnyWordInSentence:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split(" ")
        for i, w in enumerate(words):
            if w.startswith(searchWord):
                return i + 1
        return -1
